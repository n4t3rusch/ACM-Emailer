<!-- src/components/DataSender.vue -->
<template>
    <div class="data-sender">
      <input v-model="inputData" placeholder="Enter some data">
      <button @click="sendData">Send Data</button>
      <p>{{ responseMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DataSender',
    data() {
      return {
        inputData: '',
        responseMessage: ''
      }
    },
    methods: {
      sendData() {
        fetch('/api/process', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ data: this.inputData })
        })
        .then(response => response.json())
        .then(data => {
          this.responseMessage = data.message;
        })
        .catch((error) => {
          console.error('Error:', error);
          this.responseMessage = 'An error occurred';
        });
      }
    }
  }
  </script>