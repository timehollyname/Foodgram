const ingredientsContainer = document.querySelector('.form__field-group-ingredientes-container');
const inputIngredient = document.querySelector('#ingredient');
const formDropdownItems = document.querySelector('.form__dropdown-items');
const dimension = document.querySelector('#dimension');
const quantity = document.querySelector('#quantity');
const addIng = document.querySelector('#addIng');

const api = new Api(apiUrl, csrftoken);

function Ingredients() {
    const dropdown = (e) => {
        if(e.target.classList.contains('form__item-list')) {
            inputIngredient.value = e.target.textContent;
            inputIngredient.setAttribute('data-id', e.target.getAttribute('data-id'));
            formDropdownItems.style.display = ''
            dimension.textContent = e.target.getAttribute('data-dimension');
        }
    };

    const addIngredient = (e) => {
        if(inputIngredient.value && quantity.value) {
            const data = getValue();
            const searchIngredient = document.querySelector(`div[id="ing-${data.id}"]`);

            if(searchIngredient) {
                let input = searchIngredient.querySelector('input');
                let span = searchIngredient.querySelector('span:not(.form__field-item-delete)');
                let updatedQuantity = parseFloat(input.value.trim().split(' && ')[1]) + parseFloat(data.quantity);

                input.value = `${data.id} && ${updatedQuantity}`;
                span.textContent = span.textContent.replace(/\s([0-9.,]+)\s/, ` ${updatedQuantity} `);

                return;
            }

            const elem = document.createElement('div');
            elem.id = `ing-${data.id}`;
            elem.classList.add('form__field-item-ingredient');

            elem.innerHTML = `
                <span>${data.name} ${data.quantity} ${data.dimension}</span> 
                <span class="form__field-item-delete"></span>
                <input type="hidden" name="ingredients" value="${data.id} && ${data.quantity}">
            `;

            ingredientsContainer.appendChild(elem);
        }
    };

    const eventDelete = (e) => {
        if(e.target.classList.contains('form__field-item-delete')) {
            const item = e.target.closest('.form__field-item-ingredient');
            item.removeEventListener('click', eventDelete);
            item.remove();
        };
    };

    const getValue = (e) => {
        const data = {
            id: inputIngredient.getAttribute('data-id').trim(),
            name: inputIngredient.value.trim(),
            quantity: quantity.value.trim(),
            dimension: dimension.textContent.trim()
        };

        clearValue(inputIngredient);
        clearValue(quantity);

        return data;
    };

    const clearValue = (input) => {
        input.value = '';
    };

    return {
        addIngredient,
        dropdown,
        eventDelete
    };
};

const cbEventInput = (elem) => {
    return api.getIngredients(elem.target.value).then(e => {
        if(e.count > 0 ) {
            const items = e.results.map(elem => {
                return `<a class="form__item-list" data-id="${elem.id}" data-dimension="${elem.dimension}">${elem.name}</a>`
            }).join(' ');

            formDropdownItems.style.display = 'flex';
            formDropdownItems.innerHTML = items;
        }
    }).catch(e => console.log(e));
};

const eventInput = debouncing(cbEventInput, 100);
inputIngredient.addEventListener('input', eventInput);

const ingredients = Ingredients();
formDropdownItems.addEventListener('click', ingredients.dropdown);
addIng.addEventListener('click', ingredients.addIngredient);
ingredientsContainer.addEventListener('click', ingredients.eventDelete);
