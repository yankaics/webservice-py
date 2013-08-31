webservice-py
=============

herald web service by python.


===

### Curriculum Service

获取课表相关信息

**请求：**

```
GET http://herald.seu.edu.cn/herald_web_service/curriculum/一卡通号或学号/学期/

eg: http://herald.seu.edu.cn/herald_web_service/curriculum/213110561/13-14-2/
```

**响应：**


```json
[
  [
    [
      "左侧列表课程1",
      "左侧列表教师1",
      "左侧列表学分1",
      "左侧列表上课周次1"
    ],
    [
      "左侧列表课程2",
      "左侧列表教师2",
      "左侧列表学分2",
      "左侧列表上课周次2"
    ]
  ],
  [
    [//上午课程
      [	//周一上午课程
        [
          "周一上午课程1",
          "课程1 上课周次",
          "课程1 上课时间",
          "课程1 上课地点"
        ],
        [
          "周一上午课程2",
          "课程2 上课周次",
          "课程2 上课时间",
          "课程2 上课地点"
        ]
      ],
      [
        [//周二上午课程]
      ],
      [
        [//周三上午课程]
      ],
      [
        [//周四上午课程]
      ],
      [
        [//周五上午课程]
      ]
    ],
    [ //下午课程
      [
        [//周一下午课程]
      ],
      [
        [//周二下午课程]
      ],
      [
        [//周三下午课程]
      ],
      [
        [//周四下午课程]
      ],
      [
        [//周五下午课程]
      ]
    ],
    [ //晚上课程
      [//周一晚课程],
      [//周二晚课程],
      [//周三晚课程],
      [//周四晚课程],
      [//周五晚课程]
    ],
	// 周末课程
    [//周六课程],
    [//周日课程]
  ]
]
```

** 学号/一卡通号不存在返回：“没有找到该学生信息” **
