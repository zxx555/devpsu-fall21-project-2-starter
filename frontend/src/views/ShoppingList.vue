<template>
  <div class="custom-home">
    <h3 class="cover-heading">Shopping List</h3>
	<Shopping />
  </div>
</template>

<script>
import Shopping from '@/components/Shopping.vue'

export default {
  name: 'shoppinglist',
  components: {
	Shopping
  }
}
</script>