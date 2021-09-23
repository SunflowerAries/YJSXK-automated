uid = 'STUID'
psw = 'PASSWORD'

sleep_time = 5

url_vcode_post = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/login/check/login.do?timestrap='
url_vcode_get = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/login/4/vcode.do?timestamp='
url_image_get = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/login/vcode/image.do?vtoken='
url_class_get = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkCourse/loadDTHBFCourseInfo.do?_=' # DTHBF need to replace
url_class_validate = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkCourse/validateXsxkTabSfkf.do'
url_class_chs = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkCourse/choiceCourse.do?_='
url_class_res = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkCourse/loadXkjgRes.do?_='
url_csrf = 'http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkHome/gotoChooseCourse.do'

yjsxk_wanted_class = { '政治理论课': ['自然辨证法概论', '新时代中国特色社会主义理论与实践'],
                        '第一外国语': [],
                        '专业外语': [],
                        '学位基础课': [],
                        '学位专业课': [],
                        '专业选修课': [],
                        '公共选修课': [],
                        '其他可选课': [] }

qtxxk_dept = '计算机科学技术学院'
xqmc = ['邯郸校区', '江湾校区']

dept = {
    '研究生院': '000',
    '马克思主义学院': '001',
    '图书馆': '002',
    '体育教学部': '003',
    '大学英语教学部': '004',
    '艺术教育中心': '006',
    '研究生工作部': '008',
    '古籍整理研究所(中国古代文学研究中心)': '010',
    '中国语言文学系': '011',
    '外国语言文学学院': '012',
    '新闻学院': '013',
    '历史学系': '014',
    '哲学学院': '016',
    '国际关系与公共事务学院': '017',
    '数学科学学院': '018',
    '物理学系': '019',
    '现代物理研究所': '020',
    '化学系': '022',
    '计算机科学技术学院': '024',
    '法学院': '027',
    '航空航天系': '029',
    '材料科学系': '030',
    '光源与照明工程系': '031',
    '人口研究所': '035',
    '分析测试中心': '037',
    '高分子科学系': '044',
    '高等教育研究所': '046',
    '旅游学系': '050',
    '金融研究院': '051',
    '文物与博物馆学系': '054',
    '泛海国际金融学院': '066',
    '经济学院': '068',
    '管理学院': '069',
    '生命科学学院': '070',
    '信息科学与工程学院': '072',
    '社会发展与公共政策学院': '073',
    '环境科学与工程系': '074',
    '历史地理研究中心': '076',
    '国际文化交流学院': '080',
    '中华古籍保护研究院': '082',
    '文献信息中心': '083',
    '上海数学中心': '084',
    '类脑人工智能科学与技术研究院': '085',
    '工程与应用技术研究院': '086',
    '大数据学院': '098',
    '基础医学院': '101',
    '公共卫生学院': '102',
    '药学院': '103',
    '上海市第一人民医院': '110',
    '实验动物科学部': '112',
    '上海市肿瘤研究所': '113',
    '放射医学研究所': '114',
    '上海市生物医药技术研究院': '115',
    '护理学院': '117',
    '中山医院': '121',
    '华山医院': '122',
    '肿瘤医院': '123',
    '儿科医院': '124',
    '妇产科医院': '125',
    '眼耳鼻喉科医院': '126',
    '金山医院': '127',
    '华东医院': '128',
    '上海市第五人民医院': '129',
    '公共卫生临床中心': '130',
    '上海市第一妇婴保健院': '131',
    '上海市影像医学研究所': '132',
    '浦东医院': '133',
    '静安区中心医院': '134',
    '青浦区中心医院': '135',
    '闵行区中心医院': '136',
    '上海市口腔医院': '137',
    '生物医学研究院': '151',
    '脑科学研究院': '152',
    '临床医学院': '198',
    '临床医学七年制研究生': '199',
    '软件学院': '201',
    '微电子学院': '202',
    '先进材料实验室': '301',
    '大气与海洋科学系': '302',
    '浙江西湖高等研究院': '401',
    '上海市计划生育科学研究所': '115a',
    '上海市口腔病防治院': '137a',
    '全球公共政策研究院': '087',
    '代谢与整合生物学研究院': '088',
    '人类表型组研究院': '203',
}

yjsxk_map = { '政治理论课': ['Xwggk', 'zzllk', 6, { 'query_tabszwid': 1, 'pageIndex': 1, 'pageSize': 10 }],
               '第一外国语': ['Xwggk', 'dywgy', 7, { 'query_tabszwid': 2, 'pageIndex': 1, 'pageSize': 10 }],
                '专业外语': ['Xwggk', 'zywy', 7, { 'query_tabszwid': 3, 'pageIndex': 1, 'pageSize': 10 }],
                '学位基础课': ['Xwzyk', 'xwjck', 8, { 'query_tabszwid': 4, 'pageIndex': 1, 'pageSize': 10 }],
                '学位专业课': ['Xwzyk', 'xwzyk', 8, { 'query_tabszwid': 5, 'pageIndex': 1, 'pageSize': 10 }],
                '专业选修课': ['Xwzyk', 'zyxxk', 8, { 'query_tabszwid': 6, 'pageIndex': 1, 'pageSize': 10 }],
                '公共选修课': ['Ggxxk', 'ggxxk', 9, { 'lx': 9, 'pageIndex': 1, 'pageSize': 10 }],
                '其他可选课': ['Qtxxk', 'qtkxk', 10, { 'query_kkyx': dept[qtxxk_dept], 'lx': 10, 'pageIndex': 1, 'pageSize': 10 }]
            }