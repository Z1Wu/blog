---
title: "System_Analysis_hw1"
date: 2019-03-04T09:22:28+08:00
draft: false
---

# 系统分析第一次作业

## 软件工程的定义

> Software engineering is “(1) the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software, that is, the application of engineering to software,” and “(2) the study of approaches as in (1).” –– IEEE Standard 610.12


## software crisis 本质原因、表现，述说克服软件危机的方法

### 什么是软件危机

software crisis/软件危机 术语在 1968 年第一届软件工程大会提出。计算机的发展导致软件危机，软件工程的目标就是克服软件危机，构建生产软件的方法与知识体系。 1972年，Edsger Dijkstra 指出计算能力约强大，编程越是大问题。研制软件系统需要投入大量的人力和物力，但系统的质量却难以保证，也就是说，开发软件所需的高成本同产品的低质量之间有着尖锐的矛盾，这种现象就是所谓的“软件危机”。

### 本质原因

- 软件的规模越来越大，结构越来越复杂。

- 软件开发管理困难而复杂。

- 软件开发费用不断增加。

- 软件开发技术落后。

- 生产方式落后。

- 开发工具落后，生产率提高缓慢。

### 表现

1. 经费预算经常突破，完成时间一再拖延

2. 开发的软件不能满足用户要求。

3. 开发的软件可维护性差。

4. 开发的软件可靠性差。

### 克服的方法

软件工程诞生于60年代末期，它作为一个新兴的工程学科，主要研究软件生产的客观规律性，建立与系统化软件生产有关的概念、原则、方法、技术和工具，指导和支持软件系统的生产活动，以期达到降低软件生产成本 、改进软件产品质量、提高软件生产率水平的目标。软件工程学从硬件工程和其他人类工程中吸收了许多成功的经验，明确提出了软件生命周期的模型，发展了许多软件开发与维护阶段适用的技术和方法，并应用于软件工程实践，取得良好的效果。

## 软件生命周期

在时间维度，对软件项目任务进行划分，又成为软件开发过程。常见有瀑布模型、螺旋模型、敏捷的模型等。周期内有问题定义、可行性分析、总体描述、系统设计、编码、调试和测试、验收与运行、维护升级到废弃等阶段。

## SWEBoK 的 15 个知识域

SEBOK, 是 system engineering body of knowlege 的简写，包括以下的 15 个知识域（Knowledge Areas），分为两个部分，每个部分又细分成几个领域。

### 关于工程实践(pratice of software engineer)

- Software Requirements(软件需求)

- Software Design（软件设计）

- Software Construction（软件构建）

- Software Testing（软件测试）

- Software Maintenance（软件维护）

- Software Configuration Management（软件配置管理）

- Software Engineering Management（软件工程管理）

- Software Engineering Models and Methods（软件工程建模和方法）

- Software Quality（软件质量）

- Software Engineering Professional Practice（软件工程专业化实践）

### 关于软件工程的教育需求（Educational Requirements of Software Engineering）

- Software Engineering Economics（软件工程经济学）

- Computing Foundations（"计算"基础）

- Mathematical Foundations（数学基础）

- Engineering Foundations（工程基础）

## 简单解释 CMMI 的五个级别。例如：Level 1 - Initial：无序，自发生产模式。

### Level 1：完成级

在完成级水平上，企业对项目的目标与要做的努力很清晰，项目的目标得以实现。但是由于任务的完成带有很大的偶然性，企业无法保证在实施同类项目的时候仍然能够完成任务。企业在一级上的项目实施对实施人员有很大的依赖性。

### Level 2：管理级

在管理级水平上，企业在项目实施上能够遵守既定的计划与流程，有资源准备，权责到人，对相关的项目实施人员有相应的培训，对整个流程有监测与控制，并与上级单位对项目与流程进行审查。企业在二级水平上体现了对项目的一系列的管理程序。这一系列的管理手段排除了企业在一级时完成任务的随机性，保证了企业的所有项目实施都会得到成功。


### level 3：定义级。

在定义级水平上，企业不仅能够对项目的实施有一整套的管理措施，并保障项目的完成；而且，企业能够根据自身的特殊情况以及自己的标准流程，将这套管理体系与流程予以制度化这样，企业不仅能够在同类的项目上生到成功的实施，在不同类的项目上一样能够得到成功的实施。科学的管理成为企业的一种文化，企业的组织财富。

### level 4：CMMI四级，量化管理级。

在量化管理级水平上，企业的项目管理不仅形成了一种制度，而且要实现数字化的管理。对管理流程要做到量化与数字化。通过量化技术来实现流程的稳定性，实现管理的精度，降低项目实施在质量上的波动。

### level 5：优化级。

在优化级水平上，企业的项目管理达到了最高的境界。企业不仅能够通过信息手段与数字化手段来实现对项目的管理，而且能够充分利用信息资料，对企业在项目实施的过程中可能出现的次品予以预防。能够主动地改善流程，运用新技术，实现流程的优化。

## 用自己语言简述 SWEBok 或 CMMI 

### SWEBok

ACM和IEEE-CS发布的SWEBOK定义了软件工程学科，由多个工程域构成。SWEBOK还把软件工程相关学科列为知识域，它们是软件工程发展不可或缺的部分。相关学科知识域包括计算机工程、计算机科学、数学、管理学、项目管理、质量管理、系统工程学和软件人类工程学八个领域

### CMMI

CMMI 的全称为：Capability Maturity Model Integration，即能力成熟度模型集成。CMMI是CMM模型的最新版本。早期的CMMI（CMMI-SE/SW/IPPD）1.02版本是应用于软件业项目的管理方法，SEI在部分国家和地区开始推广和试用。随着应用的推广与模型本身的发展，演绎成为一种被广泛应用的综合性模型。

## 参考资料

1. https://baike.baidu.com/item/%E8%BD%AF%E4%BB%B6%E7%94%9F%E5%AD%98%E5%91%A8%E6%9C%9F

2. https://baike.baidu.com/item/%E8%BD%AF%E4%BB%B6%E5%8D%B1%E6%9C%BA

3. CMMI: https://blog.csdn.net/achang21/article/details/11702447

4. SWEBok:https://baike.baidu.com/item/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E4%B8%93%E4%B8%9A/4925780