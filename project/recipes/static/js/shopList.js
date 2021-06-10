const cardList = document.querySelector('.card-list');
const container = document.querySelector('.shopping-list');
const counterId = document.querySelector('#counter');
const api = new Api(apiUrl, csrftoken);
const header = new Header(counterId);

const shopList = new ShopList(cardList, container, header, api);
shopList.addEvent();
