from ..utils.function_utils import compute_f1_two_sets
"""
task: legal accusation prediction
metric: f1 score
法律判决预测-罪名预测
"""

option_list = ["侮辱", "违法发放贷款", "失火", "票据诈骗", "帮助犯罪分子逃避处罚", "重大责任事故", "对非国家工作人员行贿",
                   "非法制造、销售非法制造的注册商标标识", "非法制造、买卖、运输、邮寄、储存枪支、弹药、爆炸物", "非法获取公民个人信息",
                   "扰乱无线电通讯管理秩序", "非法持有、私藏枪支、弹药", "拒不执行判决、裁定", "虚开发票", "巨额财产来源不明",
                   "组织、领导、参加黑社会性质组织", "非法获取国家秘密", "以危险方法危害公共安全", "非法持有毒品",
                   "聚众扰乱公共场所秩序、交通秩序", "包庇毒品犯罪分子", "滥伐林木", "伪造公司、企业、事业单位、人民团体印章",
                   "非法占用农用地", "走私废物", "串通投标", "非法采伐、毁坏国家重点保护植物", "冒充军人招摇撞骗", "玩忽职守",
                   "重婚", "招收公务员、学生徇私舞弊", "组织、领导传销活动", "非法猎捕、杀害珍贵、濒危野生动物", "侵犯著作权",
                   "非法种植毒品原植物", "伪造、变造、买卖武装部队公文、证件、印章", "倒卖文物", "伪造、变造居民身份证", "滥用职权",
                   "诽谤", "猥亵儿童", "非法转让、倒卖土地使用权", "挪用公款", "污染环境", "出售、购买、运输假币", "敲诈勒索",
                   "高利转贷", "故意伤害", "持有、使用假币", "单位受贿", "强奸", "引诱、容留、介绍卖淫", "虐待",
                   "生产、销售伪劣农药、兽药、化肥、种子", "妨害公务", "容留他人吸毒", "拐骗儿童", "强制猥亵、侮辱妇女",
                   "非法处置查封、扣押、冻结的财产", "骗取贷款、票据承兑、金融票证", "强迫他人吸毒", "非法拘禁",
                   "非法携带枪支、弹药、管制刀具、危险物品危及公共安全", "绑架", "聚众斗殴", "破坏计算机信息系统",
                   "制造、贩卖、传播淫秽物品", "虐待被监管人", "贷款诈骗", "赌博", "徇私舞弊不征、少征税款",
                   "盗窃、抢夺枪支、弹药、爆炸物、危险物质", "故意杀人", "介绍贿赂", "提供侵入、非法控制计算机信息系统程序、工具",
                   "编造、故意传播虚假恐怖信息", "妨害作证", "强迫卖淫", "走私、贩卖、运输、制造毒品", "伪证", "拐卖妇女、儿童",
                   "过失损坏武器装备、军事设施、军事通信", "破坏广播电视设施、公用电信设施", "洗钱", "职务侵占", "倒卖车票、船票",
                   "抢劫", "侵占", "掩饰、隐瞒犯罪所得、犯罪所得收益", "徇私舞弊不移交刑事案件", "引诱、教唆、欺骗他人吸毒", "遗弃",
                   "生产、销售伪劣产品", "放火", "非法采矿", "对单位行贿", "盗窃、抢夺枪支、弹药、爆炸物", "破坏易燃易爆设备",
                   "妨害信用卡管理", "制作、复制、出版、贩卖、传播淫秽物品牟利", "金融凭证诈骗", "私分国有资产",
                   "走私国家禁止进出口的货物、物品", "假冒注册商标", "危险物品肇事", "走私普通货物、物品", "经济犯", "虚报注册资本",
                   "盗掘古文化遗址、古墓葬", "传播淫秽物品", "窝藏、包庇", "拒不支付劳动报酬", "行贿", "开设赌场", "传授犯罪方法",
                   "协助组织卖淫", "保险诈骗", "破坏生产经营", "破坏交通设施", "打击报复证人", "非法侵入住宅", "非国家工作人员受贿",
                   "过失致人重伤", "伪造、变造金融票证", "窝藏、转移、隐瞒毒品、毒赃", "帮助毁灭、伪造证据", "走私珍贵动物、珍贵动物制品",
                   "生产、销售假药", "逃税", "挪用特定款物", "聚众扰乱社会秩序", "组织、强迫、引诱、容留、介绍卖淫", "合同诈骗",
                   "非法生产、销售间谍专用器材", "破坏交通工具", "传播性病", "强迫交易", "隐匿、故意销毁会计凭证、会计帐簿、财务会计报告",
                   "非法组织卖血", "强迫劳动", "破坏电力设备", "销售假冒注册商标的商品", "收买被拐卖的妇女、儿童", "诬告陷害", "脱逃",
                   "非法经营", "徇私枉法", "信用卡诈骗", "生产、销售不符合安全标准的食品", "非法行医", "伪造货币", "动植物检疫徇私舞弊",
                   "单位行贿", "破坏监管秩序", "盗窃", "盗伐林木", "重大劳动安全事故", "非法吸收公众存款",
                   "非法制造、出售非法制造的发票", "非法狩猎", "组织卖淫", "非法买卖、运输、携带、持有毒品原植物种子、幼苗", "挪用资金",
                   "诈骗", "伪造、变造、买卖国家机关公文、证件、印章", "持有伪造的发票", "贪污", "非法生产、买卖警用装备",
                   "投放危险物质", "伪造、倒卖伪造的有价票证", "集资诈骗", "抢夺", "生产、销售有毒、有害食品", "非法捕捞水产品",
                   "过失致人死亡", "非法买卖制毒物品", "虚开增值税专用发票、用于骗取出口退税、抵扣税款发票", "寻衅滋事", "危险驾驶",
                   "故意毁坏财物", "招摇撞骗", "盗窃、侮辱尸体", "走私武器、弹药",
                   "非法收购、运输、加工、出售国家重点保护植物、国家重点保护植物制品", "非法出售发票", "劫持船只、汽车",
                   "受贿", "聚众哄抢", "交通肇事"]


def compute_ljp_accusation(data_dict):
    """Compute the F1-score The LJP_Accusation dataset a set of 189 different
    accusation types.

    A question may involve one or more accusation types. Given a list of
    accusation types from both the ground truth and the prediction, we
    compute the F1-score between these two lists.
    """
    score_list, abstentions = [], 0

    for example in data_dict:
        question, prediction, answer = example["origin_prompt"], example["prediction"], example["refr"]

        assert answer.startswith("罪名:"), f"answer: {answer} \n question: {question}"
        answer = answer.replace("罪名:", "")
        answers = answer.split(";")

        prediction_list =[]
        for option in option_list:
            if option in prediction:
                prediction_list.append(option)

        if len(prediction_list) == 0:
            abstentions += 1
        gt_set = set(answers)
        pred_set = set(prediction_list)
        score = compute_f1_two_sets(gt_set, pred_set)
        score_list.append(score)

    f1_score_average = sum(score_list) / len(score_list)
    return {"score": f1_score_average, "abstention_rate": abstentions/len(data_dict)}
