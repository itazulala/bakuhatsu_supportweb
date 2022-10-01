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
