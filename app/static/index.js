new Vue({
	el: '#ToDoList',
	data: {
		todos: [
			{text: 'Task 1'},
			{text: 'Task 2'},
			{text: 'Task 3'}
		],
	},
	ready() {

		// POST /someUrl
		this.$http.get('/api/todos/1', {foo: 'bar'}).then((response) => {

		// get status
			response.status;

		// get status text
			response.statusText;

		// get all headers
			response.headers;

		// get 'Expires' header
			response.headers['Expires'];

		// set data on vm
			this.todos = response.data;
			console.log(response.data);

		}, (response) => {
		// error callback
		});

	}
});