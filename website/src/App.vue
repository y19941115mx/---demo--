<template>
    <n-table :bordered="false" :single-line="false">
        <thead>
            <tr>
                <th>Abandon</th>
                <th>Abnormal</th>
                <th>Abolish</th>
                <th>...</th>
                <th>万事开头难</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>放弃</td>
                <td>反常的</td>
                <td>彻底废除</td>
                <td>...</td>
                <td>干！我刚才背的是啥</td>
            </tr>
            <tr>
                <td>...</td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
            </tr>
        </tbody>
    </n-table>
</template>
  
<script>
import { defineComponent } from "vue";
import { NButton, NDataTable, NSpace, NTable } from "naive-ui";


const createColumns = ({
    play
}) => {
    return [
        {
            title: "No",
            key: "no"
        },
        {
            title: "Title",
            key: "title"
        },
        {
            title: "Length",
            key: "length"
        },
        {
            title: "Action",
            key: "actions",
            render(row) {
                return h(
                    NButton,
                    {
                        strong: true,
                        tertiary: true,
                        size: "small",
                        onClick: () => play(row)
                    },
                    { default: () => "Play" }
                );
            }
        }
    ];
};

const data = [
    { no: 3, title: "Wonderwall", length: "4:18" },
    { no: 4, title: "Don't Look Back in Anger", length: "4:48" },
    { no: 12, title: "Champagne Supernova", length: "7:27" }
];

export default defineComponent({
    setup() {
        return {
            data,
            columns: createColumns({
                play(row) {
                    message.info(`Play ${row.title}`);
                }
            }),
            pagination: false
        };
    },
    components: {
        NDataTable,
        NSpace,
        NTable
    },
});
</script>