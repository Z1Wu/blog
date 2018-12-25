---
title: "Android_basic_debug"
date: 2018-09-17T15:07:33+08:00
draft: true
categories: "Andoird"
tags: ["Android", "debugging"]
---

# How to debug in AndroidStudio
this article is written to record the basic ways to debug your android applications. As we know, the Android Studio is the only offical IDE for Android applications, so this post will foucus on the debugging tool in this IDE.
## Logging


```java

// insert this line into the code where you suspect, this log will logs entire trace stacks for you. You can check the log content in the Logcat. 
Log.d(String, String, Throwable
```
> it often helps to include a stack trace. You can copy and paste lines directly from Logcat

## Debugger

### setting normal breakpoint

### setting excetion breakpoint

## Lint

Lint is a staic analyzer. Static analyzer is a tool which will inspect your code before run or compile.  


