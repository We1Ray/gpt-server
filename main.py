# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

openai.api_type = "azure"
openai.api_base = ""
openai.api_version = "2023-03-15-preview"
openai.api_key = ""


def chat_response():
    return openai.ChatCompletion.create(
        engine="polory_test",
        messages=[{"role": "system", "content": "You are an AI assistant that helps people find information."},
                  {"role": "user",
                   "content": "<script setup lang=\"ts\">\nimport { useCounterStore } from '@/stores/counter.js'\nimport { reactive } from 'vue'\n\ndefineProps<{\n  msg: string\n}>()\nconst counterStore = useCounterStore()\nconst user = reactive({\n  name: 'unknown',\n  gender: 'unknown',\n  isVIP: false\n})\n\nfunction change(value: string) {\n  user.name = value\n}\n</script>\n\n<template>\n  <div class=\"greetings\">\n    <h1 class=\"green\">{{ msg }}</h1>\n    <h3>\n      You’ve successfully created a project with\n      <a href=\"https://vitejs.dev/\" target=\"_blank\" rel=\"noopener\">Vite</a> +\n      <a href=\"https://vuejs.org/\" target=\"_blank\" rel=\"noopener\">Vue 3</a>. What's next?\n    </h3>\n  </div>\n  <div>\n    <h2>counter</h2>\n    <!-- 取得的 state 會響應式更新 -->\n    <p>{{ counterStore.count }}</p>\n    <p>{{ counterStore.doubleCount }}</p>\n    <!-- 可以呼叫 store 內定義的方法來修改 state -->\n    <button @click=\"counterStore.increment\">+</button>\n    <!-- 也可以直接修改 state -->\n    <button @click=\"counterStore.count--\">-</button>\n    <br/>\n    <input onchange=\"\"/>\n    <h2>{{ user.name }}</h2>\n  </div>\n</template>\n\n<style scoped>\nh1 {\n  font-weight: 500;\n  font-size: 2.6rem;\n  position: relative;\n  top: -10px;\n}\n\nh3 {\n  font-size: 1.2rem;\n}\n\n.greetings h1,\n.greetings h3 {\n  text-align: center;\n}\n\n@media (min-width: 1024px) {\n  .greetings h1,\n  .greetings h3 {\n    text-align: left;\n  }\n}\n</style>\n我要怎麼在input設定change"},
                 ],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(chat_response())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
