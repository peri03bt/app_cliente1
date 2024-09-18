/* MASKS FROM INPUTS */
document.addEventListener('DOMContentLoaded', function () {
    console.log("masks.js is loaded");
    var phoneInput = document.getElementById('phone');
    if (phoneInput) {
        console.log("phone input found");

        // Aplicando a máscara ao input
        Inputmask({
            mask: "(999) 999-9999",
            placeholder: "(123) 456-7890",
            clearIncomplete: true,  // Limpar se incompleto
            definitions: {
                '9': {
                    validator: "[0-9]",
                    cardinality: 1
                }
            }
        }).mask(phoneInput);

        // Garantir que apenas números sejam inseridos
        phoneInput.addEventListener('input', function (e) {
            var value = e.target.value;
            e.target.value = value.replace(/\D/g, '');
        });
    } else {
        console.log("phone input not found");
    }
});
