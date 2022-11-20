let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";
let productId = "";


document.querySelectorAll('.btn').forEach(item => {
  item.addEventListener('click', event => {
    if (tg.MainButton.isVisible) {
		tg.MainButton.hide();
	}
	else {
		tg.MainButton.setText("Вы выбрали товар 1!");
		productId = item.value ;
		tg.MainButton.show();
	}
  })
})

Telegram.WebApp.onEvent('mainButtonClicked', function(){

	tg.sendData(productId);
});





