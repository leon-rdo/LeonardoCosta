let achievementsJSON = [
    {title: 'Ganhador do Hackathon INSERN 2022', description: 'O desafio INSERN consistiu em uma competição híbrida com base num tema na qual foram desenvolvidos protótipos digitais das soluções propostas.', picture: './assets/images/Equipe-da-Unama-Ganha-Desafio-INSERN-2022.jpeg', alt: 'Equipe SERTECH da UNAMA: Leonardo e Nandara segurando um cheque gigante de R$ 15.000 com a inscrição "1º Lugar", Denis e Michel à esquerda, atrás, um carro forte da PROSSEGUR.', url: './assets/Pages/DesafioINSERN.html', date: '04/12/2022'},
    {title: 'Em breve'},
    //{title: '', description: '', picture: '/assets/images/...', url: '/assets/Pages/...', date: ''},
];

let achievementsArea = document.querySelector('.card-group');

for (let i = 0; i < achievementsJSON.length; i++) {

    let itemCard = document.querySelector('.modelo-card').cloneNode(true);
    if (achievementsJSON[i].title == 'Em breve') {
        itemCard.querySelector('.modelo-card .ratio img').src = 'https://cdn-icons-png.flaticon.com/512/148/148855.png';
        itemCard.querySelector('.modelo-card .ratio img').alt = 'Ícone de ampulheta.';
        itemCard.querySelector('.modelo-card .card-body .card-title').innerHTML = 'Em breve!';
        itemCard.querySelector('.modelo-card .card-body span').style.display = '';
        itemCard.querySelector('.modelo-card .card-body .card-text').innerHTML = 'Mais conquistas estão por vir!';
        itemCard.querySelector('.modelo-card .card-body a').href = '';
        itemCard.querySelector('.modelo-card .card-footer small').innerHTML = '';

        itemCard.querySelector('.modelo-card .card-body a').classList.add("disabled");
        itemCard.querySelector('.modelo-card .card-body a').setAttribute("aria-disabled", "true");
        itemCard.querySelector('.modelo-card .card-body a').setAttribute("role", "button");
        itemCard.querySelector('.modelo-card .card-body a').setAttribute("tabindex", "-1");
    } else {
        itemCard.querySelector('.modelo-card .ratio img').src = achievementsJSON[i].picture;
        itemCard.querySelector('.modelo-card .ratio img').alt = achievementsJSON[i].alt;
        itemCard.querySelector('.modelo-card .card-body .card-title').innerHTML = achievementsJSON[i].title;
        itemCard.querySelector('.modelo-card .card-body span').style.display = 'none';
        itemCard.querySelector('.modelo-card .card-body .card-text').innerHTML = achievementsJSON[i].description;
        itemCard.querySelector('.modelo-card .card-body a').href = achievementsJSON[i].url;
        itemCard.querySelector('.modelo-card .card-footer small').innerHTML = achievementsJSON[i].date;
    }

    achievementsArea.append(itemCard);
}