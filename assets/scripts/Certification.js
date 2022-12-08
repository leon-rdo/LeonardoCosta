let certificationJSON = [
    { title: 'PBB Practicioner', picture: './assets/images/Certificado de PBB Practitioner (Leonardo Costa).png' },
    { title: 'Trilha Conctar - RocketSeat', picture: './assets/images/Certificado Conectar (Leonardo Costa).png' },
    { title: 'Test of English as Foreign Language - TOEFL', picture: './assets/images/TOEFL - PBT (Leonardo Costa).jpg' },
    //{ title: '', picture: './assets/images/...' },
];

let certificationArea = document.querySelector('.carousel-inner');
let certificationBtn = document.querySelector('.carousel-indicators');

for (let i = 0; i < formationsJSON.length; i++) {
    let i1 = i+1

    let itemBtnSlide = document.createElement('button');
    let itemCertification = document.createElement('div');
    let imageCertification = document.createElement('img');

    if (i == 0) {
        imageCertification.src = certificationJSON[i].picture;
        imageCertification.alt = 'Certificado de ' + certificationJSON[i].title;
        imageCertification.classList.add('d-block');
        imageCertification.classList.add('w-100');
        itemCertification.classList.add('carousel-item');
        itemCertification.classList.add('ratio');
        itemCertification.classList.add('ratio-16x9');
        itemCertification.classList.add('active');

        itemBtnSlide.setAttribute('type', 'button');
        itemBtnSlide.setAttribute('data-bs-target', '#carouselExampleIndicators');
        itemBtnSlide.setAttribute('data-bs-slide-to', i);
        itemBtnSlide.setAttribute('aria-current', 'true');
        itemBtnSlide.setAttribute('aria-label', 'Slide '+i1);
        itemBtnSlide.classList.add('active');
    } else {
        imageCertification.src = certificationJSON[i].picture;
        imageCertification.alt = 'Certificado de ' + certificationJSON[i].title;
        imageCertification.classList.add('d-block');
        imageCertification.classList.add('w-100');
        itemCertification.classList.add('carousel-item');
        itemCertification.classList.add('ratio');
        itemCertification.classList.add('ratio-16x9');

        itemBtnSlide.setAttribute('type', 'button');
        itemBtnSlide.setAttribute('data-bs-target', '#carouselExampleIndicators');
        itemBtnSlide.setAttribute('data-bs-slide-to', i);
        itemBtnSlide.setAttribute('aria-current', 'true');
        itemBtnSlide.setAttribute('aria-label', 'Slide '+i1);
    }
    
    itemCertification.append(imageCertification);
    certificationArea.append(itemCertification);
    certificationBtn.append(itemBtnSlide);
}