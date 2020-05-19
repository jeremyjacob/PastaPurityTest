document.querySelector('#submit').addEventListener('click', event => {
    let checked = 0;
    document.querySelectorAll('input').forEach(element => {
        if (element.checked) {
            checked++;
        }
    });
    console.log(checked);
    document.querySelector('#content').style.display = 'none';
    document.querySelector('#instruction').style.display = 'none';
    document.querySelector('#result').style.display = 'block';
    document.querySelector('#score').innerText = 100 - checked;
});

document.querySelector('#top').addEventListener('click', event => {
    if (document.querySelector('#pee').checked == true) {
        event.preventDefault();
    }
});