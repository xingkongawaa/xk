$('year').text(new Date().getFullYear())

function toBuyMCWarn() {
  layer.open({
    title: "注意",
    type: 1,
    content: $('#buyWarn'),
    btn: '加入我的世界Q群'
    , btn1: function () {
      window.open("http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=C_t4N9xl_USdxi2YT_56WZGbr3cliGxh&authKey=AWkBAz0Jr6Byl8C6U31BByuoX2USRcDLk89EcqCfOk29Bowx120EDtMkvzGj13jy&noverify=0&group_code=77817759")
    }
  });
}

function buyWarn() {
  layer.open({
    title: "温馨提示",
    type: 1,
    content: $('#buyWarn'),
  });
}

$('.btn_s_t').click(function () {
  $('#j_b').text(this.textContent)
});