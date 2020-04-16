import Mock from 'mockjs'

Mock.mock(/getNewsList/, {
    'list|5': [{
        'url': '@url',
        'title': '@ctitle(5, 20)'
    }]
})

export default Mock