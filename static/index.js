const MDCTextField = mdc.textField.MDCTextField;

window.onload = function () {
    [].map.call(document.querySelectorAll('.mdc-text-field'), function (el) {
        return new MDCTextField(el);
    });
}

function onReturnClick() {
     window.history.back();
}