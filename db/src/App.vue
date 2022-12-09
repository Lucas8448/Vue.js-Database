<script setup>
import { useCssModule } from 'vue';

</script>

<template>
<div id="example">
  <button v-on:click="httpGet('http://127.0.0.1:5000/room/1', null)">Room</button>
  <h1>{{response}}</h1>
</div>
  
</template>

<script>
import { ref } from 'vue'
function httpGet(theUrl, data) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, true);
  xmlHttp.setRequestHeader("Access-Control-Allow-Headers", "*");
  xmlHttp.setRequestHeader("Access-Control-Allow-Origin", "*");
  xmlHttp.send(data);
  xmlHttp.onload = () => {
  if (xmlHttp.readyState === xmlHttp.DONE) {
    if (xmlHttp.status === 200) {
      console.log(xmlHttp);
      console.log(xmlHttp.responseText);
    }
  }

    console.log(xmlHttp.response);
  const resp = xmlHttp.response;

    response.value = resp
  return resp
  }
}

const response = ref("")
</script>
<style scoped>
</style>
