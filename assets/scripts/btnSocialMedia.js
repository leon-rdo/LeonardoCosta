let btnSocialMediaJSON = [
    {name: 'LinkedIn', link: 'https://www.linkedin.com/in/leonrdo-costa', icon: '../images/LinkedIn.svg'},
    {name: 'GitHub', link: 'https://github.com/leon-rdo', icon: '../images/GitHubLogo.svg'},
    {name: 'Instagram', link: 'https://www.instagram.com/leonrdo_mtheus', icon: '/assets/images/InstagramLogo.svg'},
    {name: 'Twitter', link: 'https://twitter.com/leonrdomtheus', icon: '../images/TwitterLogo.svg'},
    {name: 'Koo', link: 'https://www.kooapp.com/profile/leonardoabreu', icon: '../images/KooLogo.svg'},
    //{name: '', link: '', icon: '../images/'},
];

let btnSocialMediaArea = document.querySelector('.Box-RedesSociais');

for (let i = 0; i < btnSocialMediaJSON.length; i++) {

    let itemSocialMediaBtn = document.querySelector('.modelo-btn').cloneNode(true);
    itemSocialMediaBtn.querySelector('.modelo-btn .RedeSocialLogo').src = btnSocialMediaJSON[i].icon;
    itemSocialMediaBtn.querySelector('.modelo-btn .RedeSocialLogo').alt = 'ícone do ' + btnSocialMediaJSON[i].name;
    itemSocialMediaBtn.href = btnSocialMediaJSON[i].link;

    btnSocialMediaArea.append(itemSocialMediaBtn);
}