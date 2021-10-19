<template>
  <div class="custom-home">
    <h3 class="cover-heading">To Do list</h3>
    <List />
  </div>
</template>

<script>
import List from '@/components/List.vue'

export default {
  name: 'toDoList',
  components: {
    List
  }
}
</script>