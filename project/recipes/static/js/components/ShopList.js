class ShopList {
    constructor(cardList, container, counter, api) {
        this.cardList = cardList;
        this.container = container;
        this.counter = counter;
        this.api = api;
        this.delItem = this.delItem.bind(this);
    }

    addEvent() {
        this.container.addEventListener('click', this.delItem)
    }

    delItem(e) {
        if(e.target.classList.contains('shopping-list__button')) {
            const item = e.target.closest('.shopping-list__item');

            this.api.removePurchases(item.getAttribute('data-id')).then(e => {
                item.remove();
                this.counter.minusCounter();

                if(this.counter.counterNum < 1) {
                    this.cardList.remove();

                    let alert = document.createElement('div');
                    alert.className = 'alert';
                    alert.innerHTML = '<div class="alert-body">Список покупок пуст. Необходимо добавить хотя бы один рецепт.</div>';

                    document.querySelector('.main').appendChild(alert);
                }
            }).catch(e => {
                console.log(e);
            });
        }
    }
}
