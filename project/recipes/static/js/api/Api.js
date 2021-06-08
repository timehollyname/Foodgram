class Api {
    constructor(route) {
        this.route = route;
		this.headers = { 'Content-Type': 'application/json' };
	}

	async getPurchases() {
		let init = { headers: this.headers };
		return this.query(`purchases/`, init, true);
	}

	async addPurchases(id) {
		let body = { recipe: id };
		let init = { method: 'POST', headers: this.headers, body: JSON.stringify(body) };
		return this.query('purchases/', init, true);
	}

	async removePurchases(id) {
		let init = { method: 'DELETE', headers: this.headers };
		return this.query(`purchases/${id}/`, init, false);
	}

	async addSubscriptions(id) {
		let body = { id: id };
		let init = { method: 'POST', headers: this.headers, body: JSON.stringify(body) };
		return this.query('subscriptions/', init, true);
	}

	async removeSubscriptions(id) {
		let init = { method: 'DELETE', headers: this.headers };
		return this.query(`subscriptions/${id}/`, init, false);
	}

	async addFavorites(id) {
		let body = { id: id };
		let init = { method: 'POST', headers: this.headers, body: JSON.stringify(body) };
		return this.query('favorites/', init, true);
	}

	async removeFavorites(id) {
		let init = { method: 'DELETE', headers: this.headers };
		return this.query(`favorites/${id}/`, init, false);
	}

	async getIngredients(text) {
		let init = { headers: this.headers };
		return this.query(`ingredients/?name=${text}`, init, true);
	}

	async query(route, init, json) {
		return fetch(`${this.route}/${route}`, init).then(e => {
			if(e.ok) {
				return json ? e.json() : e;
			}
			return Promise.reject(e.statusText);
		});
	}
}
