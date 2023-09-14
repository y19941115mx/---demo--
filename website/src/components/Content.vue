<template>
    <n-space vertical :size="12">
        <n-space>
            <n-input round  placeholder="请输入英雄名称" v-model:value="heroName">
            </n-input>
            <n-button type="info" @click="handleClick">
                搜索
            </n-button>
            <n-dropdown trigger="hover" :options="options" @select="handleSelect">
                <n-button>英雄主要定位</n-button>
            </n-dropdown>
        </n-space>

        <n-data-table remote ref="table" :columns="columns" :data="data" :loading="loading" :pagination="paginationReactive"
            :row-key="rowKey" @update:page="handlePageChange" />
    
    </n-space>
</template>
  
<script setup>
import { ref, onMounted, reactive } from 'vue'
import {NDataTable, NSpace, NDropdown, NButton, NInput } from "naive-ui";
import axios from 'axios';
import { useMessage } from 'naive-ui'

const message = useMessage()

const options = ref([])
const heroName = ref("")

const data = ref([])

const loading = ref(true)

const paginationReactive = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 10,
    prefix({ itemCount }) {
        return `Total is ${itemCount}.`
    }
})

async function setRoleOptions() {
    // 发送GET请求
    const { data } = await axios.get('/api/getRole')
    options.value = data
}

async function getHerosPageList(page, pageSize = 10) {
    // 发送GET请求
    const { data:res } = await axios.get('/api/getHerosPageList', { params: {page, pageSize}})
    data.value = res.data
    paginationReactive.pageCount = res.pageCount
    paginationReactive.itemCount = res.total
    loading.value = false
}

async function getHerosByName(name) {
    // 发送GET请求
    const { data: res } = await axios.get('/api/getHerosByName', { params: { name } })
    data.value = res.data
    paginationReactive.page = 1
    paginationReactive.pageCount = 1
    paginationReactive.pageSize = res.total
    paginationReactive.itemCount = res.total
    loading.value = false
}

async function getHerosByRole(role_main) {
    // 发送GET请求
    const { data: res } = await axios.get('/api/getHerosByRole', { params: { role_main } })
    data.value = res.data
    paginationReactive.page = 1
    paginationReactive.pageCount = 1
    paginationReactive.pageSize = res.total
    paginationReactive.itemCount = res.total
    loading.value = false
}

const handleSelect = async (key) => {
    loading.value = true
    await getHerosByRole(String(key))
}

const handleClick = async () => {
    loading.value = true
    await getHerosByName(heroName.value)
}

const handlePageChange = async (currentPage) => {
    if (!loading.value) {
        loading.value = true
        paginationReactive.page = currentPage
        await getHerosPageList(currentPage, paginationReactive.pageSize)
    }
}

const rowKey = (rowData) => {
    return rowData.id
}

const columns = ref([
    {
        title: '英雄名称',
        key: 'name'
    },
    {
        title: '主要定位',
        key: 'role_main'
    },
    {
        title: '次要定位',
        key: 'role_assist'
    },
    {
        title: '最大生命值',
        key: 'hp_max'
    },
    {
        title: '最大法力值',
        key: 'mp_max'
    },
     {
        title: '攻击类型',
        key: 'attack_range'
    }
])


onMounted(async () => {
    await setRoleOptions()
    await getHerosPageList(1)
})

</script>