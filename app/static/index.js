new Vue({
	el: '#ToDoList',
	data: {
		newTodo: '',
		todos: eval("(" + todos + ")").todos,
	},
	methods: {
		addTodo: function () {
			var text = this.newTodo.trim();
			if (text) {
				this.todos.push({ text: text });
				this.newTodo = '';
				this.$http.put('/api/todos', {id: user_id, todos: {todos: this.todos}});
			};
		},
	}
});