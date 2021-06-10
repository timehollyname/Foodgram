class Api {
    constructor(route, csrftoken) {
        this.route = route;
		this.csrftoken = csrftoken;
		this.headers = { 'Content-Type': 'application/json', 'X-CSRFToken': this.csrftoken };
	}

	async addPurchases(id) {
		let body = { 'recipe': id };
		let init = { 'method': 'POST', 'headers': this.headers, 'body': JSON.stringify(body) };
		return this.query('purchases/', init);
	}

	async removePurchases(id) {
		let init = { 'method': 'DELETE', 'headers': this.headers };
		return this.query(`purchases/${id}/`, init, false);
	}

	async addSubscriptions(id) {
		let body = { 'author': id };
		let init = { 'method': 'POST', 'headers': this.headers, 'body': JSON.stringify(body) };
		return this.query('subscriptions/', init);
	}

	async removeSubscriptions(id) {
		let init = { 'method': 'DELETE', 'headers': this.headers };
		return this.query(`subscriptions/${id}/`, init, false);
	}

	async addFavorites(id) {
		let body = { 'recipe': id };
		let init = { 'method': 'POST', 'headers': this.headers, 'body': JSON.stringify(body) };
		return this.query('favorites/', init);
	}

	async removeFavorites(id) {
		let init = { 'method': 'DELETE', 'headers': this.headers };
		return this.query(`favorites/${id}/`, init, false);
	}

	async getIngredients(text) {
		let init = { 'headers': this.headers };
		return this.query(`ingredients/?search=${text}`, init);
	}

	async query(route, init, json = true) {
		return fetch(`${this.route}/${route}`, init).then(e => {
			if(e.ok) {
				return json ? e.json() : e;
			}
			return Promise.reject(e.statusText);
		});
	}
}
