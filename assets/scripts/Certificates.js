let certificatesJSON = [
    { title: 'PBB Practicioner', picture: './assets/images/Certificado de PBB Practitioner (Leonardo Costa).png' },
    { title: 'Trilha Conctar - RocketSeat', picture: './assets/images/Certificado Conectar (Leonardo Costa).png' },
    { title: 'Test of English as Foreign Language - TOEFL', picture: './assets/images/TOEFL - PBT (Leonardo Costa).jpg' },
    //{ title: '', picture: './assets/images/...' },
];

let certificatesArea = document.querySelector('.carousel-inner');
let certificatesBtn = document.querySelector('.carousel-indicators');

for (let i = 0; i < formationsJSON.length; i++) {
    let i1 = i+1

    let itemBtnSlide = document.createElement('button');
    let itemCertificates = document.createElement('div');
    let imageCertificates = document.createElement('img');

    if (i == 0) {
        imageCertificates.src = certificatesJSON[i].picture;
        imageCertificates.alt = 'Certificado de ' + certificatesJSON[i].title;
        imageCertificates.classList.add('d-block');
        imageCertificates.classList.add('w-100');
        itemCertificates.classList.add('carousel-item');
        itemCertificates.classList.add('ratio');
        itemCertificates.classList.add('ratio-16x9');
        itemCertificates.classList.add('active');

        itemBtnSlide.setAttribute('type', 'button');
        itemBtnSlide.setAttribute('data-bs-target', '#carouselExampleIndicators');
        itemBtnSlide.setAttribute('data-bs-slide-to', i);
        itemBtnSlide.setAttribute('aria-current', 'true');
        itemBtnSlide.setAttribute('aria-label', 'Slide '+i1);
        itemBtnSlide.classList.add('active');
    } else {
        imageCertificates.src = certificatesJSON[i].picture;
        imageCertificates.alt = 'Certificado de ' + certificatesJSON[i].title;
        imageCertificates.classList.add('d-block');
        imageCertificates.classList.add('w-100');
        itemCertificates.classList.add('carousel-item');
        itemCertificates.classList.add('ratio');
        itemCertificates.classList.add('ratio-16x9');

        itemBtnSlide.setAttribute('type', 'button');
        itemBtnSlide.setAttribute('data-bs-target', '#carouselExampleIndicators');
        itemBtnSlide.setAttribute('data-bs-slide-to', i);
        itemBtnSlide.setAttribute('aria-current', 'true');
        itemBtnSlide.setAttribute('aria-label', 'Slide '+i1);
    }
    
    itemCertificates.append(imageCertificates);
    certificatesArea.append(itemCertificates);
    certificatesBtn.append(itemBtnSlide);
}