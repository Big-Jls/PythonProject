
// 如果你使用的是CommonJS模块
const CryptoJS = require('crypto-js');

const r = {
    e: 'EB444973714E4A40876CE66BE45D5930', // 用于解密的密钥
    i: 'B5A8904209931867' // 用于解密的初始化向量
};

// 解密函数
function b(t) {
    var e = CryptoJS.enc.Utf8.parse(r.e);
    var n = CryptoJS.enc.Utf8.parse(r.i);

    var decrypted = CryptoJS.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return JSON.parse(decrypted.toString(CryptoJS.enc.Utf8));
}

function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}


function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = 'B3978D054A72A7002063637CCDF6B2E5' + u(t);
    return n
}

let datas = b('MZphJmFlelDpw2aSCfdFb5y2Gzdx4AtEEXvB7fXbF2GPPm0BHW6As+dkNeqYzf0fn6M4gjfCDecwrOIAdOuC1hQyzwdFGGzdC21G4mfIHEL/r3Lg4PNJoz+tSnj2YHGRJeps7xYH6g+AUOIJ9OhB44zbwyyz7N55kY0ntGTZ6Z44jId10f3dlaJngJleBgJ4GIf8ebjbNEKABzkbGgzbafpw/9RutjxSUxHM7bBqubz/7g21HIRItERxlB2xDK7rLZVGyr2EmwQLkGQ8dnLKhaJclFC0B5QrrnY8ht+SUznzlqE1ikaA6tRPELSXuyfAKdxZRAioLSfBdpcVOm0ZUpBWC9p43fosw6kz0n2XXNY/Q7kXGb3FheY6bBDjZw0l3l+GHHKiCJvHYc/nXEdRXLcdPLh4O3DhU4wgf/Kxh24henyvSWjtQP1JRlPR6i9wtykQHeS6wbnMW/vfDEHXCDtHyzPOPsj8nEI9vJw4uV6vCD0bmtdSz/h6HxTzpXyo85dl9mHYOLz1uXIbQ0zSl+5432ybu/jZ/heJ3HPNZvKST3/206qk1Ti3tj2glqBvDZu1BUdpdyX0x6OwWzu3k939FuLrB8m+te3F0cGfz8Jpnsns9GLnQ8/S5Dbhj5EmtcctVemlw/SnhpEdEw0mZsOqiBqa5UE4rWMimtao0WxAaa5CMeLlMMunADRYkoUMUECmrOAV3s84Iz/XSZhGATUcxbujiJyQa5HPXraLkUthteRWez5Dzxje8P3PsW+iSvwyTC+LGKGFMfPKyc9ciLUXPLsAX6dFFU8xcisC6oTgNU2Fnu3BlctNtTD1UYFJQfCKrBxOQvD5nOOCmRw0aDxMnhq0/U7PkbX5Wkq+vtE=')
console.log(datas)

function get_dats(data) {
    return b(data)
}

function get_sign(t) {
    return d(t)
}

