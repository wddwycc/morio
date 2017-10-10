<template>
  <div id="app">
    <el-menu theme="dark" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">New</el-menu-item>
      <el-menu-item index="2">Learn</el-menu-item>
      <el-menu-item index="3">Archive</el-menu-item>
    </el-menu>
    <router-view></router-view>
  </div>
</template>
