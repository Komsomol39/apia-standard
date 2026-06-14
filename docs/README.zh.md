# APIA — 面向 AI 智能体的 API 标准

> **用 AI 智能体能理解的格式描述公共 API 的开放标准。**

🇬🇧 [English](../README.md) · 🇷🇺 [Русский](README.ru.md) · 🇩🇪 [Deutsch](README.de.md)

---

## 为什么需要 APIA？

一个 AI 智能体想帮用户在附近找工作、查公交时刻表、找附近的药店——它必须分别学习每个 API。每个服务都有自己的格式、认证方式和分页逻辑。没有统一的契约。

**APIA 用一个 `apia.json` 清单文件解决这个问题**，告诉 AI 智能体：
- 🧠 **服务能做什么**（为 LLM 编写，而非开发者）
- 🌍 **在哪里使用**（地区、语言）
- 🔑 **如何认证**
- ⚡ **数据是实时的还是缓存的**
- 💡 **在实际场景中如何正确使用的提示**

---

## 工作原理

```
用户："帮我找附近的 Python 开发工作"
        ↓
智能体读取 APIA 注册表
        ↓
找到 hh-ru → 能力: search_vacancies
        ↓
将意图映射到 API 参数:
  text="Python", lat=55.75, lng=37.61
        ↓
调用 HH.ru API → 返回结果
        ↓
智能体回答用户
```

---

## 注册表

| 服务 | 分类 | 能力数 | 认证 | API 版本 | 最后验证 | 状态 |
|---|---|---|---|---|---|---|
| [hh.ru](../manifests/hh-ru/apia.json) | 招聘 | 5 | OAuth2 / 匿名 | v1 | 2026-06-14 | ✅ 就绪 |
| [SuperJob](../manifests/superjob/apia.json) | 招聘 | 4 | API Key / 匿名 | v2.0 | 2026-06-14 | ✅ 就绪 |
| [trudvsem.ru](../manifests/trudvsem/apia.json) | 招聘（政府） | 4 | 无需认证 | v1 | 2026-06-14 | ✅ 就绪 |
| [Яндекс.Расписания](../manifests/yandex-rasp/apia.json) | 交通 | 5 | API Key | v3.0 | 2026-06-14 | ✅ 就绪 |
| [Яндекс.Карты](../manifests/yandex-maps/apia.json) | 地图 / 地理编码 | 3 | API Key | v1.x | 2026-06-14 | ✅ 就绪 |
| [2GIS](../manifests/2gis/apia.json) | 地图 / POI | 4 | API Key | v3.0 | 2026-06-14 | ✅ 就绪 |
| [data.mos.ru](../manifests/data-mos-ru/apia.json) | 城市数据（莫斯科） | 3 | API Key | v1 | 2026-06-14 | ✅ 就绪 |

---

## 如何贡献

1. Fork 本仓库
2. 创建文件夹 `manifests/{service-id}/`
3. 参照 [HH.ru 示例](../manifests/hh-ru/apia.json) 添加 `apia.json`
4. 核心原则：`description_for_ai` 要写成向 AI 智能体解释，而不是向开发者解释
5. 提交 Pull Request

---

**APIA 是开源项目，与任何 API 提供商无关联。**