document.addEventListener('DOMContentLoaded', () => {
  function tabClick(e) {
    //クリックされたtabのデータ属性を取得
    const tabTargetData = e.currentTarget.dataset.tab;
    //クリックされたtabの親要素及びその子要素を取得
    const tabList = e.currentTarget.closest('.c-tab-navigation__container');

    const tabItems = tabList.querySelectorAll('.c-tab-navigation__item');
    //クリックされたtabと同階層にあるcontentを取得
    const tabContentItems = tabList.nextElementSibling.querySelectorAll('.c-tab-navigation__tab-panel');

    //クリックされたtabと同階層のtab及びcontentからactiveクラスを削除
    tabItems.forEach((tabItem) => {
      tabItem.classList.remove('is-active');
    });
    tabContentItems.forEach((tabContentItem) => {
      tabContentItem.classList.remove('is-show');
    });

    e.currentTarget.classList.add('is-active');
    //取得したデータ属性と同じ値を持つコンテンツにactiveクラス付与
    tabContentItems.forEach((tabContentItem) => {
      if (tabContentItem.dataset.content === tabTargetData) {
        tabContentItem.classList.add('is-show');
      }
    });
  }
  //全てのtabにイベントリスナー設定
  const tabs = document.querySelectorAll('.c-tab-navigation__item');
  tabs.forEach((tab) => {
    tab.addEventListener('click', tabClick);
  });
});

document.getElementById('js-elem'); // トリガーになる要素を取得

// フォームの値を取得する
function getFormValue (elements) {
  let parameters = []
  for (let i = 0; i < elements.length; i++) {
    if (!elements[i].id) continue
    parameters.push({param_key: elements[i].id, param_value:elements[i].value})
  }
  return parameters
}

// リクエストクエリパラメータを作成する
function createQueryParameter (parameters) {
  let queryParameter = ''
  parameters.forEach( function(value, index) {
    queryParameter += value.param_key
    queryParameter += '='
    queryParameter += value.param_value
    if (index < parameters.length - 1) queryParameter += '&'
  })
  return queryParameter
}

function sendRequest (parameter) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/api/explosion/blast_calc/?' + parameter, false);
  xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  xhr.send()
  return xhr.responseText
}

function addTableRowValue (res) {
  const body_row = document.getElementById("body_row")
  const table_body = document.getElementById("table_body")
  res.results.forEach(function(array,index)  {
    let element
    if(index === 0) {
      element = body_row
    } else {
      element = body_row.cloneNode(true)
    }
    array.forEach(function(value,index) {
      if(index === 0) {
        element.childNodes[index].innerText = value.toFixed(2)
      } else {
        element.childNodes[index].innerText = value.toExponential(2)
      }

    })
    table_body.lastChild.after(element)
  })
}

// function calculationExec () {
//   const parameter = createQueryParameter(getFormValue(document.forms[0].elements))
//   const res = JSON.parse(sendRequest(parameter))
//   console.log(res)
//   result_img.src = 'data:image/png;base64,' + res.result_img
//   addTableRowValue(res)
// }

function calculationExec () {
  const exp_weight = document.getElementById('exp_weight')
  const exp_er = document.getElementById('exp_er')
  const add_tnt = document.getElementById('add_tnt')
  const meas_points = document.getElementById('meas_points')
  const parameter = 'exp_weight=' + exp_weight.value + '&exp_er=' + exp_er.value + '&add_tnt=' + add_tnt.value + '&meas_points=' + meas_points.value

  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/api/explosion/blast_calc/?' + parameter, true);
  xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  xhr.send()
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
      const result_img = document.getElementById('result_img')
      const res = JSON.parse(xhr.responseText)
      result_img.src = 'data:image/png;base64,' + res.result_img

      const body_row = document.getElementById("body_row")
      const table_body = document.getElementById("table_body")
      res.results.forEach(function(array,index)  {
        let element
        if(index === 0) {
          element = body_row
        } else {
          element = body_row.cloneNode(true)
        }
        array.forEach(function(value,index) {
          if(index === 0) {
            element.childNodes[index].innerText = value.toFixed(2)
          } else {
            element.childNodes[index].innerText = value.toExponential(2)
          }

        })
        table_body.lastChild.after(element)
      })
    }
  }
}

