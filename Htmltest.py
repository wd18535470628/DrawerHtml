#encoding:utf-8 
import re
import time,datetime
html = '''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<meta name="data-spm" content="a213w" />
        <title>运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程 -  司法拍卖 - 阿里拍卖</title>
            <meta name="keywords" content="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程司法拍卖" />
    <meta name="description" content="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程司法拍卖，起拍价￥65,454,900 ，更多运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程拍卖信息尽在阿里拍卖；阿里拍卖是全国最大最全的司法拍卖网，确保司法拍卖的公开、公平、公正！" />
        <link rel="shortcut icon" type="image/x-icon" href="//sf.taobao.com/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="//assets.alicdn.com/plugins/opensearch/provider.xml" title="淘宝购物" />

<link rel="stylesheet" href="//g.alicdn.com/??kg/global-util/1.0.6/index-min.css,kg/tb-nav/2.4.1/index-min.css">
<style>
@font-face {
  font-family: 'iconfont-sf';
  src: url('//at.alicdn.com/t/font_1449481554_1450233.eot'); /* IE9*/
  src: url('//at.alicdn.com/t/font_1449481554_1450233.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('//at.alicdn.com/t/font_1449481554_1450233.woff') format('woff'), /* chrome、firefox */
  url('//at.alicdn.com/t/font_1449481554_1450233.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
  url('//at.alicdn.com/t/font_1449481554_1450233.svg#iconfont-sf') format('svg'); /* iOS 4.1- */
}
                    
.iconfont-sf {
    font-family: "iconfont-sf"!important;
    font-size: 12px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: .2px;
    -moz-osx-font-smoothing: grayscale;
}
@font-face {
      font-family: 'iconfont-pai';
      src: url('//at.alicdn.com/t/font_1404373372_07203.eot'); /* IE9*/
      src: url('//at.alicdn.com/t/font_1404373372_07203.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
      url('//at.alicdn.com/t/font_1404373372_07203.woff') format('woff'), /* chrome、firefox */
      url('//at.alicdn.com/t/font_1404373372_07203.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
      url('//at.alicdn.com/t/font_1404373372_07203.svg#iconfont') format('svg'); /* iOS 4.1- */
}
.iconfont-pai {
    font-family: "iconfont-pai"!important;
    font-size: 12px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: .2px;
    -moz-osx-font-smoothing: grayscale;
}
input[type="submit"],
input[type="reset"],
input[type="button"],
button {
    -webkit-appearance: none;
}
.banner66-top {
    min-width: 1190px;
}
.m-i {
    font-family: arial,tahoma,'Hiragino Sans GB',sans-serif;
}
</style>

<script src="//g.alicdn.com/??kissy/k/1.4.16/seed-min.js,kg/kmd-adapter/0.1.5/index.js,kg/kmd-adapter/0.1.5/util.js,kg/global-util/1.0.7/index-min.js,tb/tracker/4.0.1/p/index/index.js,kg/tb-nav/2.5.4/index-min.js"></script>
<script>KISSY.config({modules:{'flash':{alias:['gallery/flash/1.0/']}}});KISSY.use('kg/global-util/1.0.7/');KISSY.config({modules: {'kg/tb-nav':{alias:'kg/tb-nav/2.5.4/',requires:['kg/global-util/1.0.7/']}}});KISSY.ready(function(){KISSY.use('kg/tb-nav')});</script>
<script src="//g.alicdn.com/kissy/k/1.4.16/import-style-min.js"></script>


<script src="//g.alicdn.com/tb/sf/2.9.6/config.js"></script>
<script>
    XCake.config({
        name:'sf',
        base:'//g.alicdn.com/tb/sf/2.9.6/',
        combine:KISSY.Config.debug?false:true
    });
</script>

<script>KISSY.getScript('//g.alicdn.com/mtb/videox/0.1.35/videox-pc.js');KISSY.importStyle('sf/p/detail-nr/index');</script>
</head>
<body data-spm="6688509" class="new-sf"><script>
with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=&userid=&aplus&yunid=",id="tb-beacon-aplus",src=(location>"https"?"//s":"//a")+".tbcdn.cn/s/aplus_v2.js")
</script>

<div class="site-nav" id="J_SiteNav" data-component-config='{ "cart": "0.0.6","message": "3.4.6","umpp": "1.5.4","mini-login": "6.3.8","tb-ie-updater": "0.0.4","tbar": "2.1.0","tb-footer": "1.1.6","sidebar": "1.0.10" }' data-tbar='{ "show":true, "miniCart": "2.12.2","paramsBlackList": "_wt,seeyouagain1722","my_activity": "https:&#x2F;&#x2F;market.m.taobao.com&#x2F;apps&#x2F;abs&#x2F;5&#x2F;38&#x2F;my12?psId=58386&amp;pcPsId=58388", "venueUrl": "https:&#x2F;&#x2F;1212.taobao.com?wh_weex=true&amp;data_prefetch=true&amp;wx_navbar_transparent=true", "helpUrl": "https://consumerservice.taobao.com/online-help", "validTime":{"startTime": 1512057599, "endTime": 1513094400}, "style": {"name": "171212", "path": "kg/sidebar-style-171212/0.0.5/" }, "page":[],"blackList":[],"navDataId":{"tceSid":1182567,"tceVid":0},"pluginVersion":{ "cart":"0.2.0","history":"0.2.0","redpaper":"0.0.8","gotop":"0.2.5","help":"0.2.1","ww":"0.0.3","pagenav":"0.0.27","myasset":"0.0.9","my1212":"0.0.1","my1111":"0.2.2"}}'>
    <div class="site-nav-bd" id="J_SiteNavBd">
        
        <ul class="site-nav-bd-l" id="J_SiteNavBdL" data-spm-ab="1">
            
            
            <li class="site-nav-menu site-nav-login" id="J_SiteNavLogin" data-name="login" data-spm="754894437">
                <div class="site-nav-menu-hd">
                    <a href="//login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F" target="_top">
                        
                        <span>亲，请登录</span>
                    </a>
                    
                </div>
                
            </li>
            
            
            
            
            <li id="J_Tmsg" class="site-nav-tmsg tmsg site-nav-multi-menu J_MultiMenu" data-name="tmsg" data-spm="1997563201">
                <div class="J_Menu site-nav-menu">
                    <div class="site-nav-menu-hd J_Tmsg_Basic tmsg_basic">
                        <span class="J_Tmsg_Logo tmsg_logo_area" style="zoom:1;">
                            <span class="J_Tmsg_Logo_Loading tmsg_logo_loading"></span>
                            <span class="J_Tmsg_Logo_Icon tmsg_logo_icon site-nav-icon" style="display:none">&#xe602;</span>
                            <span class="J_Tmsg_Logo_Text tmsg_logo_text">消息</span>
                            <span class="J_Tmsg_Logo_Unread tmsg_logo_unread"></span>
                        </span>
                        
                        <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                        
                    </div>

                    <div class="site-nav-menu-bd">
                        <div class="J_Tmsg_Panel_Apps tmsg_panel_apps"></div>
                    </div>
                </div>
                <div class="J_Tmsg_Panels tmsg_panels">
                    <div class="J_Tmsg_Panel_Detail tmsg_panel_detail"></div>
                    <div class="J_Tmsg_Panel_history tmsg_panel_history"></div>
                    <div class="J_Tmsg_Panel_Strong tmsg_panel_strong"></div>
                    <div class="J_Tmsg_Panel_Setting tmsg_panel_setting"></div>
                </div>
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-mobile" id="J_SiteNavMobile" data-name="mobile" data-spm="1997563273">
                <div class="site-nav-menu-hd">
                    <a href="//www.taobao.com/m" target="_top">
                        
                        <span>手机逛淘宝</span>
                    </a>
                    
                </div>
                
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-weekend site-nav-multi-menu J_MultiMenu" id="J_SiteNavWeekend" data-name="weekend" data-spm="201711111212">
            </li>
            
            
            
        </ul>
        
        <ul class="site-nav-bd-r" id="J_SiteNavBdR" data-spm-ab="2">
            
            
            <li class="site-nav-menu site-nav-home" id="J_SiteNavHome" data-name="home" data-spm="1581860521">
                <div class="site-nav-menu-hd">
                    <a href="//www.taobao.com/" target="_top">
                        
                        <span>淘宝网首页</span>
                    </a>
                    
                </div>
                
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-mytaobao site-nav-multi-menu J_MultiMenu" id="J_SiteNavMytaobao" data-name="mytaobao" data-spm="1997525045">
                <div class="site-nav-menu-hd">
                    <a href="//i.taobao.com/my_taobao.htm" target="_top">
                        
                        <span>我的淘宝</span>
                    </a>
                    
                    <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                    
                </div>
                
                <div class="site-nav-menu-bd site-nav-menu-list">
                    <div class="site-nav-menu-bd-panel menu-bd-panel">
                    
                            <a href="//trade.taobao.com/trade/itemlist/list_bought_items.htm" target="_top">已买到的宝贝</a>
                    
                            <a href="//www.taobao.com/markets/footmark/tbfoot" target="_top">我的足迹</a>
                    
                    </div>
                </div>
                
            </li>
            
            
            
            
                <li class="site-nav-menu site-nav-cart site-nav-menu-empty site-nav-multi-menu J_MultiMenu" id="J_MiniCart" data-name="cart" data-spm="1997525049">
                    <div class="site-nav-menu-hd">
                        <a href="//cart.taobao.com/cart.htm?from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739" target="_top">
                            <span class="site-nav-icon site-nav-icon-highlight">&#xe603;</span>
                            <span>购物车</span>
                            <strong class="h" id="J_MiniCartNum"></strong>
                        </a>
                        
                        <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                        
                    </div>
                    <div class="site-nav-menu-bd">
                        <div class="site-nav-menu-bd-panel menu-bd-panel">
                        </div>
                    </div>
                </li>
            
            
            
            
            <li class="site-nav-menu site-nav-favor site-nav-multi-menu J_MultiMenu" id="J_SiteNavFavor" data-name="favor" data-spm="1997525053">
                <div class="site-nav-menu-hd">
                    <a href="//shoucang.taobao.com/item_collect.htm" target="_top">
                        <span class="site-nav-icon">&#xe604;</span>
                        <span>收藏夹</span>
                    </a>
                    
                    <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                    
                </div>
                
                <div class="site-nav-menu-bd site-nav-menu-list">
                    <div class="site-nav-menu-bd-panel menu-bd-panel">
                    
                            <a href="//shoucang.taobao.com/item_collect.htm" target="_top">收藏的宝贝</a>
                    
                            <a href="//shoucang.taobao.com/shop_collect_list.htm" target="_top">收藏的店铺</a>
                    
                    </div>
                </div>
                
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-catalog" id="J_SiteNavCatalog" data-name="catalog" data-spm="1997563209">
                <div class="site-nav-menu-hd">
                    <a href="//www.taobao.com/tbhome/page/market-list" target="_top">
                        
                        <span>商品分类</span>
                    </a>
                    
                </div>
                
            </li>
            
            
            <li class="site-nav-pipe">|</li>
            
            
            
            <li class="site-nav-menu site-nav-seller site-nav-multi-menu J_MultiMenu" id="J_SiteNavSeller" data-name="seller" data-spm="1997525073">
                <div class="site-nav-menu-hd">
                    <a href="//mai.taobao.com/seller_admin.htm" target="_top">
                        
                        <span>卖家中心</span>
                    </a>
                    
                    <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                    
                </div>
                
                <div class="site-nav-menu-bd site-nav-menu-list">
                    <div class="site-nav-menu-bd-panel menu-bd-panel">
                    
                            <a href="//mai.taobao.com/seller_admin.htm" target="_top">免费开店</a>
                    
                            <a href="//trade.taobao.com/trade/itemlist/list_sold_items.htm" target="_top">已卖出的宝贝</a>
                    
                            <a href="//sell.taobao.com/auction/goods/goods_on_sale.htm" target="_top">出售中的宝贝</a>
                    
                            <a href="//fuwu.taobao.com/?tracelog=tbdd" target="_top">卖家服务市场</a>
                    
                            <a href="//daxue.taobao.com/" target="_top">卖家培训中心</a>
                    
                            <a href="//healthcenter.taobao.com/home/health_home.htm" target="_top">体检中心</a>
                    
                            <a href="//infob.taobao.com/help" target="_top">问商友</a>
                    
                    </div>
                </div>
                
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-service site-nav-multi-menu J_MultiMenu" id="J_SiteNavService" data-name="service" data-spm="754895749">
                <div class="site-nav-menu-hd">
                    <a href="https://consumerservice.taobao.com" target="_top">
                        
                        <span>联系客服</span>
                    </a>
                    
                    <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                    
                </div>
                
                <div class="site-nav-menu-bd site-nav-menu-list">
                    <div class="site-nav-menu-bd-panel menu-bd-panel">
                    
                            <a href="https://consumerservice.taobao.com/online-help" target="_top">消费者客服</a>
                    
                            <a href="//helpcenter.taobao.com/index?from=high" target="_top">卖家客服</a>
                    
                    </div>
                </div>
                
            </li>
            
            
            
            
            <li class="site-nav-menu site-nav-sitemap site-nav-multi-menu J_MultiMenu" id="J_SiteNavSitemap" data-name="sitemap" data-spm="1997525077">
                <div class="site-nav-menu-hd">
                    <a href="https://www.taobao.com/tbhome/page/sitemap" target="_top">
                        <span class="site-nav-icon site-nav-icon-highlight">&#xe601;</span>
                        <span>网站导航</span>
                    </a>
                    
                    <span class="site-nav-arrow"><span class="site-nav-icon">&#xe605;</span></span>
                    
                </div>
                
            </li>
            
            
            
        </ul>
        
    </div>
</div>

<!--[if lt IE 8]>
<style>html,body{overflow:hidden;height:100%}</style>
<div class="tb-ie-updater-layer"></div>
<div class="tb-ie-updater-box" data-spm="20161112">
  <a href="https://www.google.cn/intl/zh-CN/chrome/browser/desktop/" class="tb-ie-updater-google" target="_blank" data-spm-click="gostr=/tbieupdate;locaid=d1;name=google">谷歌 Chrome</a>
  <a href="http://www.uc.cn/ucbrowser/download/" class="tb-ie-updater-uc" target="_blank" data-spm-click="gostr=/tbieupdate20161112;locaid=d2;name=uc">UC 浏览器</a>"
</div>
<![endif]-->
    <style>.clearfix{*zoom:1}.clearfix:after,.clearfix:before{content:" ";display:table}.clearfix:after{clear:both}.sf-head-2014{min-width:1190px;margin-bottom:20px}.sf-head-2014 .header-img{text-indent:-999em;display:block}.sf-head-2014 .nav-con{position:relative;background-color:#fff;height:40px;line-height:40px;border-bottom:1px solid #d7d7d7}.sf-head-2014 .nav-con i{position:absolute;left:-21px;height:13px;top:8px;width:1px;background-color:#ddd}.sf-head-2014 .nav-con .other-nav{padding-right:1px;position:absolute;right:210px}.sf-head-2014 .nav-con .other-nav li{position:relative;float:left;margin-right:-1px}.sf-head-2014 .nav-con .other-nav a{position:relative;font-size:14px;padding:0 5px;margin:0 15px;*margin:7px 15px 0;display:inline-block;*display:inline;*zoom:1;font-weight:700;line-height:25px;height:25px}.sf-head-2014 .nav-wrap{width:1190px;margin:0 auto;height:100%;position:relative}.sf-head-2014 .useless-border{position:absolute;bottom:-3px;left:0;width:100%;height:2px;background-color:#eee}.sf-head-2014 .main-nav{float:left}.sf-head-2014 .main-nav li{float:left;position:relative}.sf-head-2014 .main-nav .first a{padding:0 10px;margin-right:25px;margin-left:0;line-height:25px;height:25px;text-align:center}.sf-head-2014 .main-nav a{position:relative;display:inline-block;margin-left:20px;margin-right:20px;padding:0 5px;font-weight:700;font-size:14px;line-height:25px;*margin-top:7px;height:25px}.sf-head-2014 .main-nav .paimai-icon{right:-8px}.sf-head-2014 .nav-wrap a{color:#333;text-decoration:none;text-align:center;transition:all .1s linear;-webkit-transition:all .1s linear;-moz-transition:all .1s linear;-o-transition:all .1s linear}.sf-head-2014 .nav-wrap .current a,.sf-head-2014 .nav-wrap a:hover{line-height:25px;height:25px;text-align:center;background-color:#de2a23;color:#fff}.sf-head-2014 .nav-wrap li .img-nav{background:0 0}.sf-head-2014 .other-nav .icon-help{position:absolute;top:1px;left:0;font-size:20px}.sf-head-2014 .other-nav i{left:auto;right:-16px}.sf-head-2014 .other-nav .paimai-icon{right:-9px}.sf-head-2014 .p-search{position:absolute;right:0;top:3px;height:30px;line-height:30px;width:202px}.sf-head-2014 .p-search input{width:160px;padding:6px 0 6px 10px;height:16px;line-height:16px;vertical-align:middle;color:#999;outline:0;border:1px solid #d7d7d7;border-right-width:0;background-color:#fff;position:relative;left:4px}.sf-head-2014 .p-search button{cursor:pointer;width:27px;height:30px;border-width:0;border-left:1px solid #ccc;background-color:#e6e6e6;color:#878787;vertical-align:middle}.sf-head-2014 .paimai-search-form{height:30px}.sf-head-2014 .paimai-icon{position:absolute;top:5px}.sf-head-2014 .paimai-icon-big{vertical-align:middle;display:inline-block;*display:inline;*zoom:1}.shadow{-webkit-box-shadow:0 1px 3px #e9e8e8;-o-box-shadow:0 1px 3px #e9e8e8;-moz-box-shadow:0 1px 3px #e9e8e8;box-shadow:0 1px 3px #e9e8e8}</style>
<div id="sf-head-2014" class="sf-head-2014" data-spm="sfhead2014">
  
  <a href="//sf.taobao.com/" target="_self" class="header-img"
     style="height: 130px;background: url(//img.alicdn.com/tfs/TB1NhQNkxrI8KJjy0FpXXb5hVXa-1600-131.jpg) center center no-repeat #c3203b;">司法拍卖</a>
  

  <div class="nav-con">
    <div class="nav-wrap clearfix">
      <ul class="main-nav J_MainNav clearfix">
        
        <li class=" first  " data-pattern="current=index">
          
          <a class="song-ti hot-nav"
             href="//sf.taobao.com/?current=index"  target="_blank">
          首页
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="/courtList.htm|/court_list.htm">
          
          <a class="song-ti hot-nav"
             href="//sf.taobao.com/court_list.htm"  target="_blank">
          <i></i>法院
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="/noticeList.htm|/notice_list.htm">
          
          <a class="song-ti hot-nav"
             href="//sf.taobao.com/notice_list.htm"  target="_blank">
          <i></i>公告
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="/calendar.htm">
          
          <a class="song-ti hot-nav"
             href="//sf.taobao.com/calendar.htm"  target="_blank">
          <i></i>预告
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="current=jianlou">
          
          <a class="song-ti hot-nav"
             href="https:&#x2F;&#x2F;sf.taobao.com&#x2F;item_list.htm?current=jianlou&amp;circ=%2C4&amp;trade_type=1&amp;auction_start_seg=-1"  target="_blank">
          <i></i>捡漏
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="current=wanyuanhuo">
          
          <a class="song-ti hot-nav"
             href="&#x2F;&#x2F;sf.taobao.com&#x2F;list&#x2F;0.htm?userId=&amp;category=&amp;city=&amp;tradeType=&amp;province=&amp;city=&amp;sorder=&amp;stParam=&amp;startPrice=1&amp;endPrice=20000&amp;banner=million_goods&amp;current=wanyuanhuo"  target="_blank">
          <i></i>万元货
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="current=haohuo">
          
          <a class="song-ti hot-nav"
             href="https:&#x2F;&#x2F;sf.taobao.com&#x2F;item_list.htm?current=haohuo&amp;userId=&amp;category=&amp;city=&amp;tradeType=&amp;province=&amp;city=&amp;circ=&amp;sorder=&amp;stParam=&amp;spm=a213w.3064813.9001.2&amp;startPrice=50000000&amp;endPrice="  target="_blank">
          <i></i>豪货
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="">
          
          <a class="song-ti hot-nav"
             href="https://fwpm.taobao.com"  target="_blank">
          <i></i>服务
          
          <img class="paimai-icon" src="//img.alicdn.com/tps/i4/TB1_3vYKXXXXXawXXXXtKXbFXXX.gif" alt="服务"/>
          
          </a>
          
        </li>
        
        <li class=" " data-pattern="">
          
          <a class="song-ti hot-nav"
             href="//paimai.taobao.com/auctionList/my_auction_list.htm"  target="_blank">
          <i></i>我的拍卖
          
          </a>
          
        </li>
        
      </ul>
      <ul class="other-nav clearfix">
        
        
        <li class="J_OtherNavItem">
          
          <a class="song-ti img-nav" href="//zc-paimai.taobao.com/zc/index.htm"  target="_blank">
          <img src="https://img.alicdn.com/tfs/TB12vCuSXXXXXayXVXXXXXXXXXX-77-31.gif" class="paimai-icon-big" alt=""/>
          </a>
          
        </li>
        
        <li class="J_OtherNavItem">
          
          <a class="song-ti img-nav" href="//paimai.taobao.com/"  target="_blank">
          <img src="//img.alicdn.com/tps/i2/TB1MLS.IXXXXXaEXXXXRjUEJpXX-87-26.png" class="paimai-icon-big" alt=""/>
          </a>
          
        </li>
        
      </ul>
      <div class="p-search" id="J_Search" role="search">
        
        <form class="paimai-search-form" method="get" target="_blank" action="//sf.taobao.com/item_list.htm" _lpchecked="1">
          <input id="J_SearchTxt" type="text" name="q" placeholder="标的物名称/地理位置" accesskey="q" maxlength="512">
          <input type="hidden" name="spm" value="a213w.3064813.9001.1">
          <button class="J_SearchIpt search-btn iconfont-sf icon-sousuo" type="submit">
          </button>
        </form>
        
        <style>
          .sf-head-2014 .paimai-search-form .iconfont-sf {
            background: #e6e6e6 url(//img.alicdn.com/tps/i4/T1_JfZFuXeXXadE...-14-15.png) 5px 7px no-repeat;
          }
        </style>
        
        
      </div>
    </div>
    <div class="useless-border"></div>
  </div>
</div>
<script>
  (function(S) {
    S.ready(function() {
      S.use('sf-head-2014', function(S, Mod) {
        new Mod('#sf-head-2014');
      });
    })
  })(KISSY);
</script>
<script>KISSY.add("sf-head-2014",["node"],function(t,n){function a(){this.init.apply(this,arguments)}var r=n("node"),e=r.all;return a.prototype={init:function(t){var n=this;n._node=e(t),n.addCurrent(),n.initSearchText()},addCurrent:function(){var n=this,a=!1,r=location.href,i=e("li",e(".J_MainNav",n._node));i.length&&i.each(function(n){n=e(n);var i=t.trim(n.attr("data-pattern"));return i&&(i=i.split("|"),t.each(i,function(t){return r.indexOf(t)>0?(n.addClass("current").siblings().removeClass("current"),a=!0,!1):void 0})),a?!1:void 0})},initSearchText:function(){t.ready(function(){var t,n=e("#J_keywords");n.length&&(t=n.val())&&e("#J_SearchTxt").val(t)})}},a});</script>

<script>
    window.g_config = {appId: 1009, toolbar: false, startTime: new Date().valueOf()};
    window._poc = [['_setRate', 1000]];
    TB.Global.blacklist = ['fn-cart'];
    TB.Global.use('fn-browser-update', function(G, BrowserUpdate) {
        new BrowserUpdate();
    });
</script>







<input name='_tb_token_' type='hidden' value='38335f3b373eb'>
<input type="hidden" id="J_ItemId" name="itemId" value="557630794279">
<input type="hidden" id="J_Version" name="version" value="1">
<input name="auctionType" type="hidden" id="auctionType" value="">
<input name="userId" type="hidden" id="userId" value="0">
<input type="hidden" id="J_PageId" name="pageId" value="0b838ccf15209175679235177e340b">
<input type="hidden" id="J_IsSellOffNew" value="">
    
<input name="checkLoginUrl" type="hidden" id="J_CheckLoginUrl" value="//sf.taobao.com/json/check_login.do">

<input name="serverTimeGap" type="hidden" id="serverTimeGap" data-time="1520917567000" value="5"/>

<div id="page" class="sf-wrap latest-version ">
        <div class="content time-info" id="J_TimeNotSync" style="display:none;">
            提醒：您电脑时间和拍卖时间不一致，为避免错过合理的出价时间，请尽早出价！
        </div>
                    <link rel="stylesheet" type="text/css" href="//g.alicdn.com/tb-mod/pm-detail-notice/0.0.10/index.css"/>

<div id="pm-detail-notice" class="pm-detail-notice" data-expires="2017/10/10 18:00">
  <div class="detail-notice detail-notice-wrapper" style="color:red;background-color:#f1f2f4">
    <a href="https://www.taobao.com/markets/paimai/IE8" target="_blank"> 浏览器IE8、IE9将在10月后停止使用flash功能，请升级浏览器！</a>
  </div>
</div>

<script>
  (function(S){
    S.ready(function(){
      S.use('pm-detail-notice',function(S,Mod){
        new Mod('#pm-detail-notice');
      });
    })
  })(KISSY);
</script>
<script src="//g.alicdn.com/tb-mod/pm-detail-notice/0.0.10/index.js"></script>

        
        <div class="content">
        <!-- 顶部 {{{ -->
        
        <div class="browser-tips">
            <i></i>提醒：您的浏览器版本太低，可能会影响出价，建议使用Firefox、Chrome、IE9及以上浏览器 <a href="//110.taobao.com/home/software.htm?tracelog=detail_aq" target="_blank">去下载 &gt;</a><s></s>
        </div>
        
                <div class="grid-c">
            <div class="crumbs" data-spm="crumbs">
                                <a target="_blank" href="//sf.taobao.com">司法拍卖</a>
                <span class="pai-stream-arraw">></span> <a target="_blank" href="//sf.taobao.com/0351/08">山西省高级人民法院</a>
                <span class="pai-stream-arraw-current">></span> <a target="_blank" href="//sf.taobao.com/notice_detail/619653.htm">山西省高级人民法院关于运城市空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程（第一次拍卖）的公告</a>
                            </div>
            <div class="service-online">
                <img src="//img.alicdn.com/tps/i1/TB1m.bZKXXXXXcmXpXXyJ4pFFXX-23-22.png" alt="" />
                                <a target="_blank" href="//h5.m.taobao.com/alicare/alicarePC.html?from=paimai_judicial_detail_pc">在线客服(推荐)</a>
                            </div>
            <div class="service-tel"><i></i>客服专线 400-822-2870</div>
        </div>
    </div>
                
                <div class="grid-c">
            <div class="module-sf" data-spm="detail">
                <div class="pm-main clearfix">
                    <h1>【第一次拍卖】运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程
                                                            </h1>
                                        <div class="pm-main-l">
        <div class="pm-pic pm-s425">
       <img id="J_ImgBooth" src="//img.alicdn.com/bao/uploaded/i1/TB1xb9ZX3kLL1JjSZFp6sa7nFXa_460x460.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" data-haszoom="460">
    </div>
    
        <ul id="J_UlThumb" class="pm-thumb clearfix">
                                                <li class="pm-selected J_FristImg" >
                    <div class="pm-pic pm-s80 ">
                        <a href="javascript:void(0);">
                            <img src="//img.alicdn.com/bao/uploaded/i1/TB1xb9ZX3kLL1JjSZFp6sa7nFXa_80x80.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" />
                        </a>
                    </div>
                </li>
                                                            <li >
                    <div class="pm-pic pm-s80 ">
                        <a href="javascript:void(0);">
                            <img src="//img.alicdn.com/bao/uploaded/i4/3246173936/TB2f0YDXrsTMeJjy1zbXXchlVXa_!!0-paimai.jpg_80x80.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" />
                        </a>
                    </div>
                </li>
                                                            <li >
                    <div class="pm-pic pm-s80 ">
                        <a href="javascript:void(0);">
                            <img src="//img.alicdn.com/bao/uploaded/i3/3246173936/TB276O2X.EIL1JjSZFFXXc5kVXa_!!0-paimai.jpg_80x80.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" />
                        </a>
                    </div>
                </li>
                                                            <li >
                    <div class="pm-pic pm-s80 ">
                        <a href="javascript:void(0);">
                            <img src="//img.alicdn.com/bao/uploaded/i2/3246173936/TB2s5d0XEl7MKJjSZFDXXaOEpXa_!!0-paimai.jpg_80x80.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" />
                        </a>
                    </div>
                </li>
                                                            <li >
                    <div class="pm-pic pm-s80  pm-pic-last ">
                        <a href="javascript:void(0);">
                            <img src="//img.alicdn.com/bao/uploaded/i4/3246173936/TB2RNm4X8oHL1JjSZFwXXb6vpXa_!!0-paimai.jpg_80x80.jpg"  alt="运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程" />
                        </a>
                    </div>
                </li>
                        </ul>
    
        <div class="pm-remind">
        <span class="pm-apply i-b"><em class="J_Applyer">0</em> 人报名</span>
        <span class="pm-separate i-b"> </span>
                <span class="pm-reminder i-b"><em>6</em> 人设置提醒</span>
        <span class="pm-separate i-b"> </span>
                                <span class="pm-surround i-b"><em id="J_Looker">3987</em> 次围观</span>
                    </div>
    <p class="share-line">
        <a href="#" class="share-btn J_ShareBtn" target="_top" rel="nofollow" tabindex="0" aria-haspopup="0" aria-label="tab键导航" data-shareparam='{"title":"运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程",
        "type" : "item",
        "key": "557630794279",
                "client_id": 177742,                 "linkurl":"//sf.taobao.com/auction.htm?id=557630794279",
        "comment":"我正在@淘宝拍卖会 上玩拍卖，现在关注的是「运城空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程」，一旦出手，势在必得！玩儿的是心跳，拍得就是捡漏！" ,
        "itempic":"//img.alicdn.com/bao/uploaded/i1/TB1xb9ZX3kLL1JjSZFp6sa7nFXa"}'>
            <span class="iconfont-sf">&#xe61f;</span> 分享给好友
        </a>
    </p>
                                                        
        
                </div>

                                                <div class="pm-main-l auction-interaction">
                    <span class="pm-subscribe i-b J_Remind" data-config='{"outerId":"557630794279","type":2,"deposit":false,"skin":{"theme":"sf","btn":"fg"}}' ></span>
                    <ul class="pm-bid-eyebrow">
            <li id="sf-price">
                <span class="title">当前价</span>
                    <div class="price-info-wrap">
        <p class="i-info-wrap i-left">
            <span class="pm-current-price J_Price">
                <em>65,454,900 </em>
            </span>
            <em class="rmb-unit">元</em>
        </p>
        <p class="i-info-wrap i-right">
                        
                    </p>
    </div>
            </li>
            <li class="J_PItem" id="sf-countdown" data-itemId="557630794279" data-now="1520917567000" data-timeToEnd="-14526367000" data-timeToStart="-14612767000" data-end="1506391200000" data-start="1506304800000">
                <span class="title over-title">结束时间</span>
                <span  class="countdown J_TimeLeft">2017/09/26 10:00:00</span>
                <span id="J_Delay" class="pm-delay" ><em class="delayCnt">0</em>次延时</span>
            </li>
        </ul>
        <div class="pm-bid bid-over">
            <h1 class="bid-fail">
                                    本场拍卖已流拍 ！                            </h1>
                        <div class="close-price"></div>
        </div>
        <div class="my-info clearfix" id="J_User" >
            </div>
    

    <input type="hidden" id="login-url" value="https://login.taobao.com" />
    <input type="hidden" id="subscribe-url" value="//paimai.taobao.com/json/get_subscribers_num.htm?item_ids=557630794279" />
    <input type="hidden" id="stream-url" value="//sf.taobao.com/pay_foregift.htm?item_id=557630794279" />
    <input type="hidden" id="terminate-url" value="//sf.taobao.com/kill_auction.htm?item_id=557630794279" />
    <input type="hidden" id="auction-url" value="//sf.taobao.com/frame.htm?item_id=557630794279" />
    <input type="hidden" id="J_Status" value="4" />
    <input type="hidden" id="J_RuleType" value="1" />
    <input type="hidden" id="J_Polling" value="//sf.taobao.com/json/process_priority.htm?item_id=557630794279" />
    <input id="verifyAlipay" type="hidden" value="//sf.taobao.com/json/check_foregift_status.htm">
            <input type="hidden" id="auctionCategory" value="sf" />
        
                <div class="pm-bid-mouse clearfix">
        <table class="pai-pay-infor">
            <colgroup>
                <col width="37%">
                <col width="37%">
                <col width="">
            </colgroup>
            <thead>
            </thead>
            <tbody id="J_HoverShow">
            <tr>
                <td>
                                            <span class="pay-mark i-b">起 拍 价</span>
                                        <span class="pay-price" style="z-index: 99;">: <em class="m-i">&yen;</em><span class="J_Price">65,454,900 </span></span>
                </td>
                <td>
                    <span class="pay-mark i-b">加价幅度</span>
                    <span class="pay-price">: <em class="m-i">&yen;</em><span class="J_Price">50,000 </span></span>
                </td>
                <td>
                                            <span class="pay-mark i-b">类 型</span>
                        <span class=" J_Type_p ">: <span class="pay-type">拍卖</span><span class="pay-type-help"></span></span>
                                    </td>
            </tr>
            <tr>
                <td>
                    <span class="pay-mark i-b">保 证 金</span>
                    <span class="pai-save-price ">: <em class="m-i">&yen;</em><span class="J_Price">3,300,000 </span></span>
                </td>
                <td>
                    <span class="pay-mark i-b">竞价周期</span>
                    <span>: 1天</span>
                </td>
                <td class="prior-td">
                    <span class="pay-mark i-b pay-first" >优先购买权人<em class="pay-first-icon"></em></span>
                    <span>:
                        无
                                            </span>
                </td>
            </tr>
            <tr>
                                                <td>
                    <span class="pay-mark i-b">评 估 价</span>
                    <span class="pay-price" style="z-index: 99;">: <em class="m-i">&yen;</em><span class="J_Price">65,454,900</span></span>
                </td>
                                <td class="delay-td">
                    <span class="pay-mark J_Delay i-b">延时周期</span>
                    <span>: 5分钟 <span class="pay-type-help"></span></span>
                </td>
                                    <td>&nbsp;</td>
                                            </tr>
            </tbody>
        </table>
    </div>
    
        
    <div class="pai-info">
        <p>
            竞价规则：
            <span class="pai-content">
            至少一人报名且出价不低于起拍价，方可成交 
                        <span>
        </p>
        <p>
                            处置单位：
                                        <a target="_blank" href="//sf.taobao.com/0351/08">山西省高级人民法院</a>
                    </p>
        <p>联系咨询方式：<em>太原公共资源拍卖中心 史先生</em> 18635165002 / 
                    </p>
                
    </div>
</div>
<div class="pm-bid-right">
        <div class="verify-pay-result fake-hidden" id="verifyPayResult"><span>报名遇到问题</span></div>
    
                                                                                                 <div class="share-wrap">
    <div class="qr-wrap">
        <p>扫码出价</p>
        <img src="//gqrcode.alicdn.com/img?type=hv&amp;w=124&amp;h=124&amp;text=https%3A%2F%2Ftb.cn%2F12lYDcw" alt="二维码"/>
    </div>
</div>                        <div class="like-wrap">
                <h3>你可能喜欢</h3>
                                                                                                  <div class="like-item">
                                <a target="_blank" href="//sf.taobao.com/sf_item/565009638446.htm">
                                  <img src="//img.alicdn.com/bao/uploaded/i1/TB1ZzA5XY5YBuNjSspoktHeNFXa_170x10000" width="178" height="120" />
                            </a>
                            <p class="like-item-desc">
                                <a target="_blank" href="//sf.taobao.com/sf_item/565009638446.htm">位于绛县古绛镇东关村 ... </a>
                            </p>
                                                               <p class="like-item-price"> 起拍价<span class="price-green"><em>￥</em>1881490.00</span></p>
                                                    </div>
                                                                                                                        <div class="like-item">
                                <a target="_blank" href="//sf.taobao.com/sf_item/565095396742.htm">
                                  <img src="//img.alicdn.com/bao/uploaded/i1/TB1YFz0bkCWBuNjy0FayvhUlXXa_170x10000" width="178" height="120" />
                            </a>
                            <p class="like-item-desc">
                                <a target="_blank" href="//sf.taobao.com/sf_item/565095396742.htm">绛县志信小区9号楼2单 ... </a>
                            </p>
                                                               <p class="like-item-price"> 起拍价<span class="price-green"><em>￥</em>260000.00</span></p>
                                                    </div>
                                                                                                      </div>
          </div>


                    <input type="hidden" id="J_BidLoopTime" value="0" data-version="1">
                </div>
            </div>
        </div>

        
                                <!--EMS:sf/detail/pollingswitch-->
<textarea style="display:none;" id="J_IsCut">

</textarea>
                                                 <link rel='canonical' href="//sf.taobao.com/sf_item/557630794279.htm" />
                        
<div class="grid-c">
    <div class="module-sf" data-spm="tabs">
        <div id="J_FixedWrap" class="pm-addition clearfix">
            <div class="wrap-line">
                <span class="line selected1"></span>
            </div>
            <div id="J_NeedFixed" class="detail-for-remind">
                <ul class="tab-menu ks-switchable-nav" id="J_DetailTabMenu" >
                    <li class="current first"><a href="#NoticeDetail">竞买公告</a></li>
                    <li><a href="#ItemNotice">竞买须知</a></li>
                    <li><a href="#RemindTip"><s></s>标的物介绍</a></li>
                                         <li><a href="#J_RecordContent">竞买记录 (<span class="J_Record">
                                                                    0
                                                    </span>)</a></li>
                                                                                <li><a data-link="true" href="//www.taobao.com/markets/paimai/sf/detail/faq?itemId=" target="_blank"><img src="//img.alicdn.com/tfs/TB1TrrRSXXXXXc4XVXXXXXXXXXX-32-32.png" class="qa-logo" alt=""/>大家都在问</a></li>
                                    </ul>
            </div>

            <div id="J_DetailTabMain" class="detail-main">
                <div class="addition-desc J_Content">
                                                             <dd id="J_BeforeBidTipsPayMethodInner" class="hidden"><span>该标的物需缴纳保证金3,300,000  元，建议您使用网银付款，推荐：招行、浦发、宁波银行、工行（客户需为工行金牌会员）</span> <a
                            href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-sy#s3" target="_blank">查看各银行支付限额及视频教程</a></dd>
                                                    <div class="before-bid-tips" data-spm="before-bid">   <h4><span>竞拍前必读</span><a href="//www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-sy#s3" target="_blank" class="more-questions">更多常见问题</a></h4>   <div class="pai-qa">     <dl>       <dt>拍卖准备</dt>       <dd>阅读竞买公告，实地看样；确保有淘宝账号及实名认证完成的支付宝账号，<a href="//www.taobao.com/markets/paimai/qiyezhanghao" target="_blank">企业账号注册流程</a>，         <a           href="//www.taobao.com/markets/paimai/qiyezhanghao_copy2" target="_blank">个人账号注册流程</a>；拍卖过程中淘宝平台不收取任何费用</dd>     </dl>     <dl style="height: 51px;">       <dt>报名交保证金</dt>       <dd>拍卖结束前都可以交保证金，建议提前1-2天交，以免遇到问题错过拍卖；可以委托他人拍卖，<a href="//www.taobao.com/markets/paimai/sf-helpcenter-pqzb_copy" target="_blank">查看委托流程</a></dd>       <dd id="J_BeforeBidTipsPayMethod" class="tips-pay-method"></dd>     </dl>     <dl>       <dt>参与竞拍</dt>       <dd>手机电脑均可出价，出价次数无限制（可以不出价）<a href="//www.taobao.com/markets/paimai/sf-helpcenter-cyjp_copy#l3" target="_blank">查看出价、成交等规则</a></dd>     </dl>     <dl>       <dt>竞拍结束</dt>       <dd>竞拍失败：保证金会自动全额退回给竞买人。<a href="//www.taobao.com/markets/paimai/sf-helpcenter-zfjg_copy#c3" target="_blank">查看保证金退回方式</a></dd>       <dd>竞拍成功：按照法院在竞买公告中的说明支付尾款，尾款支付后请联系法院签署《拍卖成交确认书》，<a href="//www.taobao.com/markets/paimai/sf-helpcenter-zfjg_copy#c2" target="_blank">办理交割</a>。</dd>     </dl>   </div> </div>
                                                                                                </div>

                <div class="record-list J_Content" id="NoticeDetail">
                    <div class="pai-title">
                        <div class="pai-title-text">竞买公告</div>
                        <div class="pai-title-line"></div>
                    </div>
                                       <div class="sf-notice-tips" data-spm="notice-tips">
                        <p>竞拍前请务必遵照《竞买公告》的要求，进行实地看样、调查标的物信息（如过户要求、违章情况等）、了解竞买资质、委托代理及尾款支付方式等内容。</p>
                          <p class="sf-notice-tips-warning">如违反相关规定，您的保证金可能会被法院划扣并产生其他司法处罚等后果，请理性参拍！<a href="//www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-qa_copy4#c16" target="_blank">查看真实案例</a></p>
                    </div>
                                    <div id="J_NoticeDetail" class="detail-common-text" data-from="//sf.taobao.com/json/get_notice_attach.htm?project_id=619653">
                        公告详情加载中......
                    </div>
                                                            <div>
                        <h2 class="detail-common-head">优先购买权</h2>
                        <ul class="pri-lists-wrap">
                                                    无
                                            </div>
                                        <div class="detail-adjunct">
                        <h2 class="detail-common-head">相关附件</h2>
                        <ul id="J_DownLoadSecond" dowload-url="//sf.taobao.com/download_attach.do">
                            附件加载中......
                        </ul>
                    </div>
                </div>

                <div class="record-list J_Content" id="ItemNotice">
                    <div class="pai-title">
                        <div class="pai-title-text">竞买须知</div>
                        <div class="pai-title-line"></div>
                    </div>
                    <div id="J_ItemNotice" class="detail-common-text" data-from="//sf.taobao.com/get_notice.htm?t_name=TB1o6iiXy0TMKJjSZFNBS5_1FXa&amp;snt_name=null" >
                                                                                    拍卖须知加载中......
                                                                        </div>
                </div>

                <div class="addition-desc J_Content">
                    <div class="pai-title" id="RemindTip">
                        <div class="pai-title-text">标的物介绍</div>
                        <div class="pai-title-line"></div>
                    </div>
                                        <h2 class="detail-common-head">具体描述</h2>
                                                                        <div class="detail-common-text">
                                <span class="desc-att">相关附件下载：</span>
                                                                    <span id="J_DownLoadFirst" class="desc-att-wrap" data-from="//sf.taobao.com/json/get_gov_attach.htm?id=557630794279" dowload-url="//sf.taobao.com/download_attach.do">附件加载中......</span>
                                                            </div>
                                                <div id="J_desc" class="detail-common-text clearfix"  data-from="//desc.alicdn.com/i7/550/630/557630794279/TB1aVqdXEFWMKJjSZFv8quenFla.desc%7Cvar%5Edesc%3Bsign%5E147cef7ffb148aa601ac936655d33347%3Blang%5Egbk%3Bt%5E1503626634">
                                                            标的物详情加载中......
                                                    </div>
                                        <div class="video-img">
                        <div class="sf-pic-slide clearfix">
                                                                                                
                                                                                   <div class="slide-bigpic">
                                 <img src="//img.alicdn.com/tps/i2/TB1SN33GVXXXXarapXX0deX8pXX-900-600.png" data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1xb9ZX3kLL1JjSZFp6sa7nFXa_960x960.jpg" />
                               </div>
                                                                                                                <div class="slide-bigpic">
                                 <img src="//img.alicdn.com/tps/i2/TB1SN33GVXXXXarapXX0deX8pXX-900-600.png" data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3246173936/TB2f0YDXrsTMeJjy1zbXXchlVXa_!!0-paimai.jpg_960x960.jpg" />
                               </div>
                                                                                                                <div class="slide-bigpic">
                                 <img src="//img.alicdn.com/tps/i2/TB1SN33GVXXXXarapXX0deX8pXX-900-600.png" data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3246173936/TB276O2X.EIL1JjSZFFXXc5kVXa_!!0-paimai.jpg_960x960.jpg" />
                               </div>
                                                                                                                <div class="slide-bigpic">
                                 <img src="//img.alicdn.com/tps/i2/TB1SN33GVXXXXarapXX0deX8pXX-900-600.png" data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3246173936/TB2s5d0XEl7MKJjSZFDXXaOEpXa_!!0-paimai.jpg_960x960.jpg" />
                               </div>
                                                                                                                <div class="slide-bigpic">
                                 <img src="//img.alicdn.com/tps/i2/TB1SN33GVXXXXarapXX0deX8pXX-900-600.png" data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3246173936/TB2RNm4X8oHL1JjSZFwXXb6vpXa_!!0-paimai.jpg_960x960.jpg" />
                               </div>
                                                                             </div>
                    </div>
                    <h2 class="detail-common-head">所在地</h2>
                    <div class="detail-common-text"  >
                                                    标的物所在地：山西 运城 盐湖 运城市空港新区东环路以西一宗国有出让住宅用地使用权及地面4、5、8、9号楼在建工程
                                            </div>
                    
                                        <p style="color:red;margin: 10px 0;">地图标注仅供参考，具体位置以标的物实际为准</p>
                    <script src="//webapi.amap.com/maps?v=1.3&key=c98eaa6b4ee2957ec8eb365a6d3d9d9f"></script>
                    <div class="clearfix " id="show-part">
                        <div id="result"  name="result"> </div>
                        <div id="J_Map" class="show-amap"></div>
                        <input type="hidden" id="J_Coordinate" name="coordinate" value="111.004657,35.019149"  >
                    </div>
                                    </div>

                                 <div class="introduce-bid J_Content"  id="J_RecordContent" has-data="0" data-from="//sf.taobao.com/json/get_bid_records.htm?id=557630794279&amp;records_type=pageRecords">
                    <div class="pai-title">
                        <div class="pai-title-text">竞买记录</div>
                        <div class="pai-title-line"></div>
                    </div>
                    <table class="record-table" id="J_RecordList">
                        <thead>
                            <tr>
                                <th >状态</th>
                                <th class="bid-number">竞买号</th>
                                <th class="offer-price">价格</th>
                                <th class="price-time">时间</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>

                    <ul class="page-nav" id="J_PageContent">
                        <li><a class="pagebutton" href="#" style="display: none;">上一页</a></li>
                        <li><a class="pagebutton" href="#" style="display: none;">下一页</a></li>
                    </ul>
                </div>
                
                            </div>
        </div>
                <div id="J_ServiceBlockWrap"></div>
    </div>
</div>

            </div>
</div>



<link rel="stylesheet" type="text/css" href="//g.alicdn.com/tb-mod/ems-sf-detail-fixed-server/0.0.4/index.css"/>
<div id="ems-sf-detail-fixed-server" class="ems-sf-detail-fixed-server">
  <div class="wrap">
  
  <a href="&#x2F;&#x2F;www.taobao.com&#x2F;markets&#x2F;paimai&#x2F;sf-qa-jump?spm=a213w.3064813.0.0.FBrEfL&amp;wh_ttid=pc" target="_blank" class="link0">
    <div class="pic-wrap">
      <img class="pic" src="https://img.alicdn.com/tfs/TB171w0cWagSKJjy0FgXXcRqFXa-78-78.png" alt="" width="30" height="30"/>
      <img class="hover-pic" src="//img.alicdn.com/tfs/TB1SnH2d3MPMeJjy1XdXXasrXXa-48-48.png" alt="" width="30" height="30"/>
    </div>
    <div class="name">体验参拍</div>
  </a>
  
  <a href="https://h5.m.taobao.com/alicare/alicarePC.html?from=paimai_judicial_detail_pc" target="_blank" class="link1">
    <div class="pic-wrap">
      <img class="pic" src="https://img.alicdn.com/tfs/TB1AEs3c6ihSKJjy0FlXXadEXXa-78-78.png" alt="" width="30" height="30"/>
      <img class="hover-pic" src="//img.alicdn.com/tfs/TB18D_2d3MPMeJjy1XdXXasrXXa-48-48.png" alt="" width="30" height="30"/>
    </div>
    <div class="name">咨询客服</div>
  </a>
  
  </div>
</div>
<!--http://ems.alibaba-inc.com/sites/design/pm/daily/detail/to-top-->
<link rel="stylesheet" type="text/css" href="//g.alicdn.com/tb-mod/pai-to-top/0.0.4/index.css"/>
<div id="pai-to-top" class="pai-to-top sf-pai-to-top" style="bottom: 70px;">
    <div class="module-wrap">
        
        
        <a class="to-top to-top-box" href="javascript:void(0);">
            <i class="iconfont-pai">顶</i><em>回到顶部</em>
        </a>
        
    </div>
</div>
<script>
  (function(S){
    S.ready(function(){
      S.use('pai-to-top',function(S,Mod){
        new Mod('#pai-to-top');
      });
    })
  })(KISSY);
</script>
<script src="//g.alicdn.com/tb-mod/pai-to-top/0.0.4/index.js"></script>

<style type="text/css">
.pai-to-top{visibility: hidden!important; pointer-events: none;}
.sf-pai-to-top{visibility: visible!important;pointer-events: auto!important;}
</style>


<script>
    window.g_config = window.g_config || {};
    window.g_config.appStartTime = new Date().valueOf();
    KISSY.use('sf/p/detail-nr/',function(S,Page){
        Page.init();
    });
</script>
    <!--TMS:1495800-->
<link rel="stylesheet" href="//atp.alicdn.com/tmse/7/dpl/??mkt-sidebar/v3/mkt-sidebar.css" />

<link rel="stylesheet" href="//atp.alicdn.com/tmse/7/dpl/??5552/mkt-sidebar/mkt-sidebar/v3/skin/default.css" />


<div class="skin-default" data-name="mkt-sidebar" data-skin="default" data-guid="14177696725030" id="guid-14177696725030" data-version="3" data-type="3" data-hidden="true"><div class="mkt-sidebar tb-finish" style="display:none"></div></div>

<script src="//atp.alicdn.com/tmse/7/dpl/??mkt-sidebar/v3/mkt-sidebar.js"></script>

<script>KISSY.use("node",function(S){S.all('#guid-14177696725030').each(function(a){var b=a.attr("data-name"),c=a.one("."+b);c.hasClass("tb-finish")||S.use(b,function(b,d){new d(a[0],c[0])})})});</script>

<link rel="stylesheet" type="text/css" href="//g.alicdn.com/tb-mod/sf-foot-2014/0.0.5/index.css"/>


<div id="sf-foot-2014" class="sf-foot-2014">
  <div class="sf-foot-2014-list-wrap">
        <div class="sf-foot-2014-list">
            <a class="bottom-code">
                <img src="https://img.alicdn.com/tps/TB1uyuULpXXXXXpaXXXXXXXXXXX-200-217.png" >
            </a>
        
          <div class="bottom-list-row row0">
            <h3 class="ya-hei">司法学堂</h3>
            <ul>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-sy#s1">什么是司法拍卖</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-jmlc#m2">司法拍卖竞拍流程</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-mcjs#m3">如何提交保证金</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-jmlc#m5">司法拍卖出价延时</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-jmlc#m8">优先购买权人</a>
                </li>
              
            </ul>
          </div>
        
          <div class="bottom-list-row row1">
            <h3 class="ya-hei">竞买人帮助</h3>
            <ul>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://fwpm.taobao.com">金融【贷款】服务</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/qiyezhanghao?spm=a213w.6688509.detail.21.kAc0oK">企业账号注册流程</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-jmlc#m2">司法拍卖竞拍流程</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-jmlc#m3">司法拍卖出价规则</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-sy#s3https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-sy#s3">常见问题必看</a>
                </li>
              
            </ul>
          </div>
        
          <div class="bottom-list-row row2">
            <h3 class="ya-hei">支付帮助</h3>
            <ul>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-mcjs#m3">如何报名交保证金</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-mcjs#m4">交保遇到限额</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-mcjs#m2">报名交保时间</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-qa_copy4#c2">出局者保证金退回银行卡</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https://www.taobao.com/markets/paimai/sf-helpcenter?path=sf-helpcenter-qa_copy4#c1">尾款如何支付</a>
                </li>
              
            </ul>
          </div>
        
          <div class="bottom-list-row row3">
            <h3 class="ya-hei">法院服务</h3>
            <ul>
              
                <li>
                  <i></i>
                  <a target="_blank" href="//sf.taobao.com/settled.htm">入驻司法拍卖</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="https:&#x2F;&#x2F;www.taobao.com&#x2F;markets&#x2F;paimai&#x2F;sf-fyhelp?spm=0.0.0.0.rix55D&amp;path=sf-fyhelpcenter-qa#r9">法院入驻联系方式</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="//sf.taobao.com/console/index.htm">法院后台登陆</a>
                </li>
              
                <li>
                  <i></i>
                  <a target="_blank" href="//www.taobao.com/markets/paimai/sf-fyhelp">法院帮助中心</a>
                </li>
              
            </ul>
          </div>
        
        </div>
    </div>
</div>
<script>
  (function(S){
    S.ready(function(){
      S.use('sf-foot-2014',function(S,Mod){
        new Mod('#sf-foot-2014');
      });
    })
  })(KISSY);
</script>
<script src="//g.alicdn.com/tb-mod/sf-foot-2014/0.0.5/index.js"></script>


<div id="footer">
        <div id="server-num">govauction010179034088.s.et2</div>
</div>

</body>
</html>
'''
my_dict = {}
my_dict['corporate_agent'] = re.findall(re.compile(r' <p>[^\x00-\xff]{7,7}<em>(.*?)</em>', re.S), html.decode('utf8'))[0]
phoneList =  re.findall(re.compile(r'<p>[^\x00-\xff]{7,7}<em>[^\x00-\xff]{0,}.*?</em>.*?(1[34578]\d{9}/[0-9]{3,4}-[0-9]{7,8}|[0-9]{3,4}-[0-9]{7,8}|0\d{2,3}\d{7,8}|1[3578]\d{9}|147\d{8}|\d{7}).*?</p>', re.S), html.decode('utf8'))
my_dict['phone'] = ""
if phoneList.__len__() != 0:
    my_dict['phone'] = re.findall(re.compile(r'<p>[^\x00-\xff]{7,7}<em>[^\x00-\xff]{0,}.*?</em>.*?(1[34578]\d{9}/[0-9]{3,4}-[0-9]{7,8}|[0-9]{3,4}-[0-9]{7,8}|0\d{2,3}\d{7,8}|1[3578]\d{9}|147\d{8}|\d{7}).*?</p>', re.S), html.decode('utf8'))[0]
#my_dict['phone2'] = re.findall(re.compile(r'class="pai-info".*?(1[34578]\d{9}/[0-9]{3,4}-[0-9]{7,8}|[0-9]{3,4}-[0-9]{7,8}|0\d{2,3}\d{7,8}|1[358]\d{9}|147\d{8}).*?</p>', re.S), html.decode('utf8'))
print 'name:'+my_dict['corporate_agent']
print 'phone:'+my_dict['phone']
time_from = time.strftime('%Y-%m-%d', time.localtime(time.time() - 172800))
time_to = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
times = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time = time.strftime('%Y-%m-%d', time.localtime(time.time() - 86400))
print time_from
print time_to
print times
print time








