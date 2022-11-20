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
		tg.MainButton.setText("Siz 1 dona mahsulot tanladingiz!");
		productId = item.value ;
		tg.MainButton.show();
	}
  })
})

Telegram.WebApp.onEvent('mainButtonClicked', function(){
	tg.sendData(productId);
});





