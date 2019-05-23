from OrderStatus import OrderStatus
import json
class ParseJsonAndCreateMoudle:
    def __init__(self,filepath):
        self._filepath=filepath
    def parseJson(self,filepath):
        EntityMode = {}  # 实体模型结构
        ModeField = []  # 模型字段结构
        ListTemp = []  # 字段列表
        ExtendedAttributes = []  # 可扩展字段
        with open(filepath, 'r', encoding='UTF-8') as f:
            json_str = json.load(f)  # json_str是转换后的字典
            keys = [i for i in json_str.keys()][:5]
            values = [i for i in json_str.values()][:5]
            EntityMode = dict(zip(keys, values))
            EntityFieldCollection = json_str['EntityFieldCollection']  # 实体属性
            for EntityField in EntityFieldCollection:  # 每一个EntityField是一个属性
                ListTemp.append(EntityField['FieldCode'])
                for EntityFieldKey in EntityField:  # 每一个EntityFieldKey是一个属性定义
                    ModeField.append(EntityFieldKey)
                    if (isinstance(EntityField[EntityFieldKey], dict)):
                        FieldConstraint = EntityField[EntityFieldKey]
                        for Constraint in FieldConstraint:  # 每一个Constraint是一个属性限制条件
                            ExtendedAttributes.append(Constraint)
            EntityMode["EntityFieldCollection"] = ListTemp
        return EntityMode, set(ModeField), set(ExtendedAttributes), EntityFieldCollection


    def creat_moudle(self):
        EntityMode, ModeField, ExtendedAttributes, EntityFieldCollection= self.parseJson(self._filepath)
        Attribute = EntityMode['EntityFieldCollection']
        in_do = "" # 参数列表

        # 组装数据
        with open(EntityMode['EntityCode'] + ".py", "a+") as f:
            f.write("import time\n")
            f.write("class " + EntityMode['EntityCode'] + ":\n")
            # 构造函数
            for i in Attribute:
                in_do += "%s, " % i
            f.write("   def __init__(self, %s):\n" % in_do[:-2])

            for item in Attribute:
                f.write("       self.%s = %s\n" % (item, item))
            f.write("\n")


            for item in EntityFieldCollection:
                x=item['FieldCode']
                f.write('   @property\n')
                f.write("   def %s(self):\n" %x)
                f.write("       return self.%s\n" %x)
                f.write("\n")


            for item in EntityFieldCollection:
                x = item['FieldCode']
                checkStr=""
                FieldType = item['FieldType']
                if FieldType=='int':
                    checkStr+=("not isinstance(%s, int)"%x)
                elif FieldType=='string':
                    checkStr += ("not isinstance(%s, str)" % x)
                elif FieldType=='double':
                    checkStr += ("not isinstance(%s, float)" % x)
                elif FieldType=='bool':
                    checkStr += ("not isinstance(%s, bool)" % x)
                elif FieldType=='DateTime':
                    checkStr += ("not isinstance(%s, time)" % x)
                constraint = item.get('FieldConstraint')
                if constraint!=None:
                    print(constraint)
                    IsEmpty = constraint.get("IsEmpty")
                    if IsEmpty and IsEmpty=='false': # 非空
                        checkStr+=(' or %s == " "'%x)
                    IsEnum = constraint.get("IsEnum")
                    if IsEnum and IsEnum=='true': # 枚举
                        checkStr+=(' or %s != %s and %s != %s'%(x,OrderStatus.Status_0.value[0],x,OrderStatus.Status_1.value[0]))
                    Length = constraint.get("Length")
                    if Length:
                        checkStr += (' or %s.__str__().__len__() !=%s' % (x,Length))
                    MaxLength = constraint.get("MaxLength")
                    MinLength = constraint.get("MinLength")
                    if MaxLength and MinLength:
                        # or name.__len__() < 1 or name.__len__() > 50
                        checkStr += (' or %s.__len__() <%s or %s.__len__() >%s' % (x, MinLength, x, MaxLength))
                f.write('   @%s.setter\n'%x)
                f.write("   def %s(self,%s):\n" % (x,x))
                f.write("       if "+checkStr+":\n")
                f.write('           raise TypeError("%s is error!!")\n'%x)
                f.write("       self.%s = %s\n" % (x,x))
                f.write("\n")



if __name__ == '__main__':
    t = ParseJsonAndCreateMoudle('order.json')
    t.creat_moudle()