<script setup>
import { useCssModule } from 'vue';

</script>

<template>

<h3>Hello, {{uname}}</h3>
<input v-model="uname" placeholder="enter name" autocomplete="on" autocorrect="on">
<button @click="username(uname)">Submit</button>
<div class="page">
<ol>
  <li v-for="r in rooms" @click="httpGet('http://127.0.0.1:5000/rooms/' + r[0], null)"  class="rooms">
      Room {{ r[0] }}
  </li>
  <li class="rooms" @click="httpGet('http://127.0.0.1:5000/add_room', null), setTimeout(httpGet('http://127.0.0.1:5000/rooms/' + room[0], null), 50)">
    Add room
  </li>
</ol>
<div class="room-about">
  <div class="room-title">
    <h1>Room: {{ room[0] }}</h1>
    <h3>Please leave a reaction:</h3>
  </div>
  <div class="smile" @click="react(room[0], 1, uname), httpGet('http://127.0.0.1:5000/rooms/' + room[0], null)">
    <img src="./assets/images/smile.png" alt="smile">
    <h4>{{ room [1] }}</h4>
  </div>
  <div class="heart" @click="react(room[0], 2, uname), httpGet('http://127.0.0.1:5000/rooms/' + room[0], null)">
    <img src="./assets/images/heart.png" alt="heart">
    <h4>{{ room [2] }}</h4>
  </div>
  <div class="up" @click="react(room[0], 3, uname), httpGet('http://127.0.0.1:5000/rooms/' + room[0], null)">
    <img src="./assets/images/up-arrow.png" alt="up">
    <h4>{{ room [3] }}</h4>
  </div>
  <div class="down" @click="react(room[0], 4, uname), httpGet('http://127.0.0.1:5000/rooms/' + room[0], null)">
    <img src="./assets/images/down-arrow.png" alt="down">
    <h4>{{ room [4] }}</h4>
  </div>
  <div>
    <h3>Previous</h3>
    <h4>{{room[5]}}</h4>
    <h4>{{room[6]}}</h4>
    <h4>{{room[7]}}</h4>
    <h4>{{room[8]}}</h4>
    <h4>{{room[9]}}</h4>
  </div>
</div>
</div>
</template>

<script>
import { ref } from 'vue'
export default {
  created() {
    httpGet('http://127.0.0.1:5000/rooms/0', null)
  },
  methods: {
    username(name) {
      console.log("updating uname to: " + name)
      uname.value = name
    },
  }
};

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
  const resp = JSON.parse(xmlHttp.response);

    room.value = resp.room
    rooms.value = resp.rooms
  return resp
  }
}

function react(room, reaction) {
  console.log(room, reaction, uname)
  const name = uname._value
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", 'http://127.0.0.1:5000/react/' + room + '/' + name + '/' + reaction, true);
  xmlHttp.setRequestHeader("Access-Control-Allow-Headers", "*");
  xmlHttp.setRequestHeader("Access-Control-Allow-Origin", "*");
  xmlHttp.send(null);
  if (xmlHttp.readyState === xmlHttp.DONE) {
    if (xmlHttp.status === 200) {
      console.log(xmlHttp);
      console.log(xmlHttp.responseText);
      room.value = xmlHttp.responseText
    }
  }
}

const uname = ref("user")
const rooms = ref("")
const room = ref("")
</script>
