# sendtoWeCom
低版本grafana使用原生webhook调用企微发送告警。

企业微信发送应用消息参考文档：https://developer.work.weixin.qq.com/document/path/90250#%E6%8E%A5%E5%8F%A3%E5%AE%9A%E4%B9%89



### 配置文件：config.json

| 配置项        | 说明               |
| ------------- | ------------------ |
| bind          | 监听IP             |
| port          | 监听端口           |
| route         | url路由            |
| wecom.agentid | 应用ID             |
| wecom.secret  | 应用ID对应的Secret |
| wecom.cropid  | 企业ID             |
| wecom.touser  | 接收人             |
| wecom.toparty | 部门ID             |

