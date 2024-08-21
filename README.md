#

Dify 是一个开源的 LLM 应用开发平台。其直观的界面结合了 AI 工作流、RAG 管道、Agent、模型管理、可观测性功能等，让您可以快速从原型到生产。以下是其核心功能列表：
</br> </br>

**1. 工作流**: 
  在画布上构建和测试功能强大的 AI 工作流程，利用以下所有功能以及更多功能。


  https://github.com/langgenius/dify/assets/13230914/356df23e-1604-483d-80a6-9517ece318aa



**2. 全面的模型支持**: 
  与数百种专有/开源 LLMs 以及数十种推理提供商和自托管解决方案无缝集成，涵盖 GPT、Mistral、Llama3 以及任何与 OpenAI API 兼容的模型。完整的支持模型提供商列表可在[此处](https://docs.dify.ai/getting-started/readme/model-providers)找到。

![providers-v5](https://github.com/langgenius/dify/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)


**3. Prompt IDE**: 
  用于制作提示、比较模型性能以及向基于聊天的应用程序添加其他功能（如文本转语音）的直观界面。

**4. RAG Pipeline**: 
  广泛的 RAG 功能，涵盖从文档摄入到检索的所有内容，支持从 PDF、PPT 和其他常见文档格式中提取文本的开箱即用的支持。

**5. Agent 智能体**: 
  您可以基于 LLM 函数调用或 ReAct 定义 Agent，并为 Agent 添加预构建或自定义工具。Dify 为 AI Agent 提供了50多种内置工具，如谷歌搜索、DALL·E、Stable Diffusion 和 WolframAlpha 等。

**6. LLMOps**: 
  随时间监视和分析应用程序日志和性能。您可以根据生产数据和标注持续改进提示、数据集和模型。

**7. 后端即服务**: 
  所有 Dify 的功能都带有相应的 API，因此您可以轻松地将 Dify 集成到自己的业务逻辑中。


## 功能比较
<table style="width: 100%;">
  <tr>
    <th align="center">功能</th>
    <th align="center">Dify.AI</th>
    <th align="center">LangChain</th>
    <th align="center">Flowise</th>
    <th align="center">OpenAI Assistant API</th>
  </tr>
  <tr>
    <td align="center">编程方法</td>
    <td align="center">API + 应用程序导向</td>
    <td align="center">Python 代码</td>
    <td align="center">应用程序导向</td>
    <td align="center">API 导向</td>
  </tr>
  <tr>
    <td align="center">支持的 LLMs</td>
    <td align="center">丰富多样</td>
    <td align="center">丰富多样</td>
    <td align="center">丰富多样</td>
    <td align="center">仅限 OpenAI</td>
  </tr>
  <tr>
    <td align="center">RAG引擎</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td align="center">Agent</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td align="center">工作流</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
  </tr>
  <tr>
    <td align="center">可观测性</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
    <td align="center">❌</td>
  </tr>
  <tr>
    <td align="center">企业功能（SSO/访问控制）</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
    <td align="center">❌</td>
    <td align="center">❌</td>
  </tr>
  <tr>
    <td align="center">本地部署</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
  </tr>
</table>

## 使用 Dify
- **自托管 Dify 社区版</br>**
使用这个[入门指南](#quick-start)快速在您的环境中运行 Dify。
使用我们的[文档](https://docs.dify.ai)进行进一步的参考和更深入的说明。

- **面向企业/组织的 Dify</br>**
我们提供额外的面向企业的功能。[给我们发送电子邮件](mailto:business@dify.ai?subject=[GitHub]Business%20License%20Inquiry)讨论企业需求。 </br>
  > 对于使用 AWS 的初创公司和中小型企业，请查看 [AWS Marketplace 上的 Dify 高级版](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6)，并使用一键部署到您自己的 AWS VPC。它是一个价格实惠的 AMI 产品，提供了使用自定义徽标和品牌创建应用程序的选项。

## 保持领先

在 GitHub 上给 Dify Star，并立即收到新版本的通知。

![star-us](https://github.com/langgenius/dify/assets/13230914/b823edc1-6388-4e25-ad45-2f6b187adbb4)

## 安装社区版

### 系统要求

在安装 Dify 之前，请确保您的机器满足以下最低系统要求：

- CPU >= 2 Core
- RAM >= 4GB

### 快速启动

启动 Dify 服务器的最简单方法是运行我们的 [docker-compose.yml](docker/docker-compose.yaml) 文件。在运行安装命令之前，请确保您的机器上安装了 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)：

```bash
cd docker
cp .env.example .env
docker compose up -d
```

运行后，可以在浏览器上访问 [http://localhost/install](http://localhost/install) 进入 Dify 控制台并开始初始化安装操作。

### 自定义配置

如果您需要自定义配置，请参考 [.env.example](docker/.env.example) 文件中的注释，并更新 `.env` 文件中对应的值。此外，您可能需要根据您的具体部署环境和需求对 `docker-compose.yaml` 文件本身进行调整，例如更改镜像版本、端口映射或卷挂载。完成任何更改后，请重新运行 `docker-compose up -d`。您可以在[此处](https://docs.dify.ai/getting-started/install-self-hosted/environments)找到可用环境变量的完整列表。

#### 使用 Helm Chart 部署

使用 [Helm Chart](https://helm.sh/) 版本或者 YAML 文件，可以在 Kubernetes 上部署 Dify。

- [Helm Chart by @LeoQuote](https://github.com/douban/charts/tree/master/charts/dify)
- [Helm Chart by @BorisPolonsky](https://github.com/BorisPolonsky/dify-helm)
- [YAML 文件 by @Winson-030](https://github.com/Winson-030/dify-kubernetes)

#### 使用 Terraform 部署

##### Azure Global
使用 [terraform](https://www.terraform.io/) 一键部署 Dify 到 Azure。
- [Azure Terraform by @nikawang](https://github.com/nikawang/dify-azure-terraform)