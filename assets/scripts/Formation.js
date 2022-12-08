let formationsJSON = [
    { institute: 'Instituto Federal do Pará', course: 'Técnico em Eletrônica', startYear: 2018, endYear: 2021, icon: './assets/images/IFPA (Logo).svg' },
    { institute: 'Aslan Idiomas', course: 'Inglês Anvançado', startYear: 2016, endYear: 2021, icon: './assets/images/Aslan (Logo).svg' },
    { institute: 'Universidade da Amazônia', course: 'Análise e Desenvolvimento de Sistemas', startYear: 2022, endYear: 2023, icon: 'assets/images/UNAMA (Logo).svg' },
    //{name: '', link: '', icon: './assets/images/images/'},
];

let formationArea = document.querySelector('.formation-box');

for (let i = 0; i < formationsJSON.length; i++) {

    let div = document.createElement('div');

    let itenFormation = document.querySelector('.modelo-formation').cloneNode(true);
    itenFormation.querySelector('.modelo-formation .text-white').innerHTML = formationsJSON[i].course + ' - ' + formationsJSON[i].institute + ' (' + formationsJSON[i].startYear + ' - ' + formationsJSON[i].endYear + ')';
    itenFormation.querySelector('.modelo-formation .formationLogo').src = formationsJSON[i].icon;
    itenFormation.querySelector('.modelo-formation .formationLogo').alt = 'ícone de ' + formationsJSON[i].institute;
    formationArea.append(div);

    formationArea.append(div);
    div.append(itenFormation);
}