<!-- src/components/HelloFlask.vue -->
   <template>
     <div class="hello-flask">
       <h1>{{ message }}</h1>
     </div>
   </template>

   <script>
   export default {
     name: 'HelloFlask',
     data() {
       return {
         message: 'Loading...'
       }
     },
     mounted() {
       fetch('/api/hello')
         .then(response => response.json())
         .then(data => {
           this.message = data.message
         })
         .catch(error => {
           console.error('Error:', error)
           this.message = 'Failed to load message'
         })
     }
   }
   </script>