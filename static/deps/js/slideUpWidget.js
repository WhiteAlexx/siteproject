// Build: 'sdk-1.3.4-1'
(()=>{var b=(l,t,i)=>new Promise((d,r)=>{var a=c=>{try{g(i.next(c))}catch(h){r(h)}},u=c=>{try{g(i.throw(c))}catch(h){r(h)}},g=c=>c.done?d(c.value):Promise.resolve(c.value).then(a,u);g((i=i.apply(l,t)).next())});typeof document!="undefined"&&document.head.appendChild(document.createElement("style")).appendChild(document.createTextNode(`.slide-up-widget {
  overflow-x: hidden;
  overflow-y: auto;
  position: fixed;
  bottom: 0;
  left: 1px;
  right: 1px;
  height: 99%;
  max-width: 100vw;
  background: #fff;
  z-index: 999999999;
  color: #000;
  padding: 20px 15px;
  font-weight: 700;
  border-radius: 25px 25px 0 0;
  -webkit-box-shadow: 0 0 10px -5px #000;
  box-shadow: 0 0 10px -5px #000;
  font-size: 13px;
  font-family: "Helvetica Neue", Helvetica, sans-serif;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

.slide-up-widget__header {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  font-weight: 400;
  margin-bottom: 7px;
}

.slide-up-widget__title {
  text-decoration: none;
  margin: 20px 10px 10px;
  font-size: 13px;
}

.slide-up-widget__header-close-btn {
  width: 25px;
  height: 25px;
  background: #e4e4e4;
  position: absolute;
  right: 20px;
  content: "1";
  border-radius: 50%;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  line-height: 1;
  font-size: 15px;
  cursor: pointer;
  color: rgba(72, 72, 72, 0.6);
  font-family: serif;
}

.slide-up-widget__header-image {
  max-width: 100px;
  margin-bottom: 5px;
  border-radius: 10px;
  overflow: hidden;
}

.slide-up-widget__header-image svg {
  display: block;
  width: 100%;
}

.slide-up-widget__header-text {
  max-width: 240px;
  text-align: center;
  line-height: 16px;
}

.slide-up-widget__bank {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  background: red;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  background: #f4f4f4;
  padding: 10px;
  border-radius: 15px;
  margin-bottom: 10px;
  min-height: 60px;
  color: #000;
}

.slide-up-widget__bank--hide,
.slide-up-widget__title--hide {
  display: none;
}

.slide-up-widget__bank-logo {
  margin-right: 10px;
  max-width: 50px;
  border-radius: 10px;
}

.slide-up-widget__input {
  width: 100%;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  margin-bottom: 10px;
  background-color: #f4f4f4;
  padding: 15px 8px;
  outline: 0;
  border: none;
  border-radius: 8px;
}

.slide-up-widget__empty {
  font-size: 12px;
  font-weight: 400;
  padding: 0 10px;
}
`));var L=(l,t)=>{if(T(t)){let d=t.webClientUrl.endsWith("/");return`${t.webClientUrl}${d?"":"/"}${l.transactionID}${l.searchString}`}return`${t.schema}://${l.universalLinkWOProtocol}`},T=l=>!!l.webClientUrl&&(l.isWebClientActive===!0||l.isWebClientActive==="true");var S=(l,t)=>{var a;let i=new URL(l),d=(a=i.pathname.split("/").pop())!=null?a:"",r=new URL(t!=null?t:i.origin);return r.pathname=d,r.search=i.search,r.hash=i.hash,{transactionID:d,searchString:r.search,universalLink:r.href,universalLinkWOProtocol:C(r)}},C=l=>l.href.replace(`${l.protocol}//`,"");var M="qr",w="sub";function y(l){return`https://${l}.nspk.ru/proxyapp/c2bmembers.json`}function _(l){if(!/https:\/\/(qr|sub).nspk.ru\/\w{0,32}(\?)?/.test(l))throw new Error("invalidURLString");return l.indexOf("sub.nspk.ru")===-1?M:w}var m=class{static get ENTER_BANK_NAME(){return"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043D\u0430\u0437\u0432\u0430\u043D\u0438\u0435 \u0431\u0430\u043D\u043A\u0430"}static get PAYMENT_TITLE(){return"\u0412\u044B\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0430\u043D\u043A \u0434\u043B\u044F \u043F\u043E\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043D\u0438\u044F \u043E\u043F\u043B\u0430\u0442\u044B"}static get SUBSCRIPTION_TITLE(){return"\u0412\u044B\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0430\u043D\u043A \u0434\u043B\u044F \u043F\u0440\u0438\u0432\u044F\u0437\u043A\u0438 \u0441\u0447\u0451\u0442\u0430"}static get NO_MATCHING_ITEMS(){return"\u041F\u043E \u0412\u0430\u0448\u0435\u043C\u0443 \u0437\u0430\u043F\u0440\u043E\u0441\u0443 \u0440\u0435\u0437\u0443\u043B\u044C\u0442\u0430\u0442\u043E\u0432 \u043D\u0435 \u043D\u0430\u0439\u0434\u0435\u043D\u043E"}};var E='data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="239" height="120" fill="none">%0A  <path%0A    d="M211.439 33.692V63.03h-10.476V42.45h-10.087v20.58H180.4V33.69h31.039z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M158.885 64.079c9.378 0 16.342-5.75 16.342-14.467 0-8.437-5.138-13.915-13.725-13.915-3.963 0-7.233 1.395-9.696 3.802.588-4.975 4.795-8.607 9.427-8.607 1.069 0 9.117-.017 9.117-.017l4.551-8.709s-10.104.23-14.801.23c-10.732.187-17.981 9.942-17.981 21.79 0 13.803 7.07 19.893 16.766 19.893zm.057-20.668c3.482 0 5.896 2.288 5.896 6.2 0 3.521-2.145 6.422-5.896 6.43-3.588 0-6.002-2.688-6.002-6.37 0-3.913 2.414-6.26 6.002-6.26z"%0A    fill="%23000"%0A  />%0A  <path%0A    d="M133.592 53.208s-2.474 1.426-6.169 1.696c-4.248.126-8.033-2.557-8.033-7.324 0-4.65 3.34-7.315 7.926-7.315 2.812 0 6.532 1.949 6.532 1.949s2.722-4.995 4.132-7.493c-2.582-1.957-6.021-3.03-10.021-3.03-10.095 0-17.914 6.582-17.914 15.83 0 9.366 7.349 15.795 17.914 15.601 2.953-.11 7.027-1.147 9.51-2.742l-3.877-7.172z"%0A    fill="%23000"%0A  />%0A  <path d="M0 26.12l14.532 25.975v15.844L.017 93.863 0 26.12z" fill="%235B57A2" />%0A  <path%0A    d="M55.797 42.643l13.617-8.346 27.868-.026-41.485 25.414V42.643z"%0A    fill="%23D90751"%0A  />%0A  <path%0A    d="M55.72 25.967l.077 34.39-14.566-8.95V0l14.49 25.967z"%0A    fill="%23FAB718"%0A  />%0A  <path%0A    d="M97.282 34.271l-27.869.026-13.693-8.33L41.231 0l56.05 34.271z"%0A    fill="%23ED6F26"%0A  />%0A  <path%0A    d="M55.797 94.007V77.322l-14.566-8.78.008 51.458 14.558-25.993z"%0A    fill="%2363B22F"%0A  />%0A  <path%0A    d="M69.38 85.737L14.531 52.095 0 26.12l97.223 59.583-27.844.034z"%0A    fill="%231487C9"%0A  />%0A  <path%0A    d="M41.24 120l14.556-25.993 13.583-8.27 27.843-.034L41.24 120z"%0A    fill="%23017F36"%0A  />%0A  <path%0A    d="M.017 93.863l41.333-25.32-13.896-8.526-12.922 7.922L.017 93.863z"%0A    fill="%23984995"%0A  />%0A  <path%0A    d="M119.393 82.775c-.32.408-.741.716-1.246.924a4.282 4.282 0 01-1.632.316 4.63 4.63 0 01-1.633-.274 3.623 3.623 0 01-1.262-.782 3.539 3.539 0 01-.824-1.224 4.173 4.173 0 01-.295-1.589c0-.54.093-1.04.286-1.514.185-.475.454-.882.791-1.224.337-.349.741-.615 1.195-.823.463-.2.968-.308 1.523-.308.598 0 1.153.075 1.658.224.505.15.934.4 1.287.75l-.614 1.04a2.886 2.886 0 00-1.027-.6 3.612 3.612 0 00-1.119-.174c-.336 0-.656.066-.967.191a2.591 2.591 0 00-.825.533 2.438 2.438 0 00-.564.832c-.143.324-.21.682-.21 1.081 0 .408.075.774.218 1.09.144.325.337.6.581.832.244.234.53.408.858.525.329.125.674.183 1.044.183.454 0 .867-.092 1.22-.267a3.05 3.05 0 00.926-.69l.631.948zM121.126 83.84v-7.405h1.33v5.517l4.325-5.517h1.33v7.406h-1.33v-5.517l-4.325 5.517h-1.33zM136.921 82.775a3.01 3.01 0 01-1.245.924 4.291 4.291 0 01-1.633.316 4.628 4.628 0 01-1.632-.274 3.627 3.627 0 01-1.263-.782 3.539 3.539 0 01-.824-1.224 4.173 4.173 0 01-.295-1.589c0-.54.093-1.04.286-1.514.186-.475.455-.882.791-1.224.337-.349.741-.615 1.195-.823a3.637 3.637 0 011.523-.308c.598 0 1.153.075 1.658.224.505.15.934.4 1.288.75l-.615 1.04a2.874 2.874 0 00-1.026-.6 3.616 3.616 0 00-1.119-.174 2.603 2.603 0 00-1.793.724 2.536 2.536 0 00-.564.832c-.143.324-.21.682-.21 1.081 0 .408.076.774.219 1.09.143.325.336.6.58.832.244.234.531.408.859.525.328.116.673.183 1.043.183.455 0 .859-.092 1.22-.267a3.05 3.05 0 00.926-.69l.631.948zM137.603 76.435h6.824v1.315h-2.743v6.09h-1.33v-6.09h-2.743v-1.315h-.008z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M150.638 83.766c.505-.158.934-.4 1.304-.732l-.404-1.032c-.244.217-.572.4-.967.55-.396.15-.842.224-1.33.224-.732 0-1.338-.191-1.818-.582-.479-.392-.74-.94-.799-1.64h5.756c.059-.258.084-.549.084-.89 0-.508-.093-.965-.278-1.381a3.277 3.277 0 00-.74-1.074 3.295 3.295 0 00-1.111-.69 3.692 3.692 0 00-1.355-.25c-.623 0-1.17.108-1.649.308a3.637 3.637 0 00-1.204.824 3.477 3.477 0 00-.748 1.223 4.272 4.272 0 00-.261 1.514c0 .583.101 1.115.286 1.59a3.5 3.5 0 00.808 1.223c.345.34.765.599 1.262.782a4.772 4.772 0 001.658.274 5.04 5.04 0 001.506-.24zm-3.366-5.7c.412-.374.959-.557 1.649-.557.648 0 1.17.175 1.549.525.379.349.58.832.614 1.447h-4.544a2.26 2.26 0 01.732-1.414z"%0A    fill="%23000"%0A  />%0A  <path%0A    d="M154.273 76.435h1.212l2.878 3.67 2.726-3.67h1.178v7.406h-1.329v-5.4l-2.592 3.436h-.051l-2.692-3.437v5.4h-1.33v-7.405z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M165.885 76.46a4.187 4.187 0 00-1.144.49l.353 1.05c.303-.15.606-.275.909-.383.303-.109.69-.159 1.153-.159.37 0 .665.059.892.175.227.108.395.275.513.475.118.2.194.449.236.74.042.291.059.607.059.949a2.28 2.28 0 00-.909-.375 5.229 5.229 0 00-.959-.1c-.396 0-.766.059-1.12.158-.353.1-.656.25-.9.45a2.14 2.14 0 00-.589.74 2.3 2.3 0 00-.219 1.007c0 .724.211 1.29.631 1.69.421.399.976.598 1.666.598.623 0 1.12-.108 1.498-.324.379-.217.682-.466.901-.749v.957h1.245v-4.543c0-.966-.21-1.714-.639-2.239-.421-.524-1.17-.79-2.23-.79-.472 0-.918.066-1.347.183zm2.223 6c-.303.216-.699.315-1.187.315-.429 0-.766-.108-1.001-.316-.236-.216-.354-.499-.354-.849 0-.207.042-.382.135-.54.093-.158.219-.283.362-.383a1.6 1.6 0 01.513-.225c.194-.05.387-.075.589-.075.657 0 1.22.158 1.683.491v.94a3.824 3.824 0 01-.74.641zM181.841 73.83c.269-.124.521-.332.757-.64l-.724-1.04c-.185.25-.395.424-.631.516a4.007 4.007 0 01-.774.216l-.252.045c-.219.038-.454.08-.707.122a5.224 5.224 0 00-1.178.366c-.598.258-1.077.607-1.439 1.048-.362.441-.648.94-.842 1.49a7.793 7.793 0 00-.395 1.722c-.068.6-.101 1.173-.101 1.722 0 .708.092 1.348.277 1.922.186.575.446 1.057.791 1.448.345.4.758.7 1.246.916.488.216 1.035.324 1.649.324.564 0 1.086-.108 1.557-.308a3.758 3.758 0 001.212-.823c.336-.342.606-.75.791-1.207.193-.458.286-.949.286-1.465 0-.557-.084-1.064-.244-1.514a3.271 3.271 0 00-.69-1.156 3.072 3.072 0 00-1.103-.75 3.827 3.827 0 00-1.447-.266c-.32 0-.631.042-.934.125a3.604 3.604 0 00-.842.358 3.2 3.2 0 00-.698.54c-.202.209-.37.442-.488.708h-.034c.026-.341.068-.69.143-1.048.076-.358.185-.7.329-1.024.143-.324.328-.616.555-.882a2.52 2.52 0 01.875-.624 4.646 4.646 0 011.153-.374l.264-.048c.263-.048.514-.094.754-.144.32-.066.614-.15.884-.274zm-4.679 7.115a4.146 4.146 0 01-.185-1.298 2.09 2.09 0 01.303-.707c.143-.225.328-.424.547-.6a2.773 2.773 0 011.733-.59c.783 0 1.372.241 1.784.716.413.482.615 1.081.615 1.805 0 .358-.068.683-.185.982a2.36 2.36 0 01-1.279 1.323c-.303.133-.632.2-1.002.2s-.707-.075-1.018-.225a2.34 2.34 0 01-.8-.624 3.129 3.129 0 01-.513-.982zM193.563 76.435h-1.33v7.406h1.33v-7.406zm-8.281 0h1.33v2.222h1.229c.58 0 1.051.075 1.43.216.379.142.682.333.909.566.227.233.387.508.48.815.092.308.143.624.143.957 0 .333-.051.65-.16.966-.101.316-.278.59-.514.84-.235.25-.555.45-.959.6-.404.149-.892.232-1.481.232h-2.415v-7.414h.008zm1.33 3.461v2.713h.968c.665 0 1.136-.116 1.405-.35.27-.233.404-.565.404-1.006 0-.45-.143-.79-.412-1.024-.278-.233-.741-.35-1.38-.35h-.985v.017z"%0A    fill="%23000"%0A  />%0A  <path%0A    d="M202.357 82.775c-.32.408-.741.716-1.246.924a4.286 4.286 0 01-1.632.316 4.63 4.63 0 01-1.633-.274 3.613 3.613 0 01-1.262-.782 3.555 3.555 0 01-.825-1.224 4.192 4.192 0 01-.294-1.589c0-.54.092-1.04.286-1.514.185-.475.454-.882.791-1.224.337-.349.74-.615 1.195-.823a3.634 3.634 0 011.523-.308c.597 0 1.153.075 1.658.224.505.15.934.4 1.287.75l-.614 1.04a2.886 2.886 0 00-1.027-.6 3.612 3.612 0 00-1.119-.174c-.336 0-.656.066-.968.191a2.587 2.587 0 00-.824.533 2.52 2.52 0 00-.564.832c-.143.324-.21.682-.21 1.081 0 .408.075.774.218 1.09.143.325.337.6.581.832.244.234.53.408.858.525.329.116.674.183 1.044.183.454 0 .858-.092 1.22-.267a3.05 3.05 0 00.926-.69l.631.948zM203.038 76.435h6.825v1.315h-2.744v6.09h-1.329v-6.09h-2.743v-1.315h-.009z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M212.64 76.436h-1.33v10.7h1.33V83.5c.269.175.589.3.959.383.37.083.757.124 1.153.124.589 0 1.119-.108 1.599-.307a3.825 3.825 0 001.228-.84c.345-.359.606-.775.791-1.266.185-.49.278-1.015.278-1.572 0-.55-.084-1.057-.244-1.515a3.524 3.524 0 00-.69-1.181 2.996 2.996 0 00-1.086-.774 3.49 3.49 0 00-1.439-.283c-.521 0-1.009.1-1.472.3-.463.2-.825.44-1.077.74v-.873zm.926 1.373c.379-.2.791-.3 1.237-.3.387 0 .732.058 1.044.183.303.125.555.3.766.533.21.233.37.5.471.815.109.316.16.658.16 1.032 0 .4-.068.757-.185 1.09a2.4 2.4 0 01-.514.849 2.36 2.36 0 01-.816.557 2.685 2.685 0 01-1.086.208c-.361 0-.698-.041-1.018-.124a3.328 3.328 0 01-.984-.45v-3.67c.235-.282.547-.523.925-.723zM228.847 76.435h-1.33v7.406h1.33v-7.406zm-8.289 0h1.33v2.222h1.228c.581 0 1.052.075 1.431.216.379.142.682.333.909.566.227.233.387.508.479.815.093.308.143.624.143.957 0 .333-.05.65-.159.966-.101.316-.278.59-.514.84-.235.25-.555.45-.959.6-.404.149-.892.232-1.481.232h-2.415v-7.414h.008zm1.339 3.461v2.713h.968c.664 0 1.136-.116 1.405-.35.269-.233.404-.565.404-1.006 0-.45-.143-.79-.412-1.024-.278-.233-.741-.35-1.38-.35h-.985v.017z"%0A    fill="%23000"%0A  />%0A  <path%0A    d="M235.226 80.005l2.844 3.836h-1.632l-2.197-2.996-2.23 2.996h-1.548l2.827-3.77-2.659-3.636h1.633l2.028 2.796 2.061-2.796h1.549l-2.676 3.57zM118.409 92.994h-4.081v6.174h-1.33v-7.405h6.74v7.405h-1.329v-6.174zM127.286 93.077h-2.625l-.085 1.248c-.092 1.057-.218 1.906-.395 2.554-.177.65-.396 1.149-.648 1.498-.252.35-.547.591-.884.708a3.06 3.06 0 01-1.085.183l-.101-1.282c.143.008.311-.025.496-.108.186-.083.371-.266.547-.54.177-.284.337-.683.48-1.199.143-.524.236-1.206.286-2.064l.135-2.305h5.209v7.406h-1.33v-6.1z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M132.201 91.78c-.43.116-.817.282-1.145.49l.354 1.049c.303-.15.606-.275.908-.383.303-.108.691-.158 1.153-.158.371 0 .665.058.892.174.228.109.396.275.514.475.117.2.193.45.235.74.042.292.059.608.059.949a2.277 2.277 0 00-.909-.374 5.22 5.22 0 00-.959-.1c-.395 0-.766.058-1.119.158-.354.1-.657.25-.901.45a2.14 2.14 0 00-.589.74 2.3 2.3 0 00-.218 1.007c0 .723.21 1.29.631 1.689.42.399.976.599 1.666.599.623 0 1.119-.108 1.498-.325.378-.216.681-.466.9-.749v.957h1.246v-4.543c0-.965-.211-1.714-.64-2.238-.421-.525-1.17-.79-2.23-.79a5.1 5.1 0 00-1.346.182zm2.23 5.998c-.302.217-.698.317-1.186.317-.438 0-.766-.108-1.001-.317-.236-.216-.354-.499-.354-.848 0-.208.042-.383.135-.541.092-.158.219-.283.362-.383.143-.1.319-.175.513-.225a2.33 2.33 0 01.589-.074c.656 0 1.22.158 1.683.49v.94a3.83 3.83 0 01-.741.641z"%0A    fill="%23000"%0A  />%0A  <path%0A    d="M137.72 91.763h6.825v1.314h-2.744v6.091h-1.329v-6.09h-2.743v-1.315h-.009z"%0A    fill="%23000"%0A  />%0A  <path%0A    fill-rule="evenodd"%0A    clip-rule="evenodd"%0A    d="M150.756 99.093c.505-.158.934-.4 1.304-.732l-.404-1.032c-.244.217-.572.4-.968.55-.395.15-.841.224-1.329.224-.732 0-1.338-.191-1.818-.582-.48-.391-.74-.94-.799-1.64h5.756c.058-.257.084-.549.084-.89 0-.507-.093-.965-.278-1.381a3.264 3.264 0 00-.741-1.073 3.28 3.28 0 00-1.11-.691 3.696 3.696 0 00-1.355-.25c-.623 0-1.17.108-1.649.308a3.618 3.618 0 00-1.204.824 3.494 3.494 0 00-.749 1.223 4.294 4.294 0 00-.261 1.514c0 .583.101 1.115.286 1.59.186.474.463.882.808 1.223.345.341.766.599 1.263.782a4.766 4.766 0 001.657.275c.497 0 1.002-.084 1.507-.242zm-3.374-5.708c.412-.374.959-.557 1.649-.557.657 0 1.17.183 1.549.524.378.35.58.832.614 1.448h-4.544a2.26 2.26 0 01.732-1.415zM153.23 91.763h1.683l2.566 3.57-2.743 3.835h-1.632l2.877-3.836-2.751-3.57zm4.577 0h1.33v7.405h-1.33v-7.405zm6.084 7.405l-2.928-3.836 2.735-3.57h-1.65l-2.583 3.57 2.777 3.836h1.649zM169.967 99.093c.505-.158.934-.4 1.304-.732l-.404-1.032c-.244.217-.572.4-.967.55-.396.15-.842.224-1.33.224-.732 0-1.338-.191-1.818-.582-.479-.391-.74-.94-.799-1.64h5.756c.059-.257.084-.549.084-.89 0-.507-.092-.965-.278-1.381a3.276 3.276 0 00-.74-1.073 3.284 3.284 0 00-1.111-.691 3.692 3.692 0 00-1.355-.25c-.622 0-1.169.108-1.649.308a3.624 3.624 0 00-1.203.824 3.465 3.465 0 00-.749 1.223 4.272 4.272 0 00-.261 1.514c0 .583.101 1.115.286 1.59.185.474.463.882.808 1.223.345.341.765.599 1.262.782a4.772 4.772 0 001.658.275 5.04 5.04 0 001.506-.242zm-3.374-5.708c.413-.374.96-.557 1.65-.557.648 0 1.169.183 1.548.524.379.35.581.832.614 1.448h-4.544a2.26 2.26 0 01.732-1.415zM177.188 89.275c-.783 0-1.212-.433-1.279-1.298h-1.254c0 .332.059.632.168.915.11.283.27.524.48.724.21.2.48.358.791.482.311.125.673.183 1.085.183.379 0 .716-.058 1.019-.183.303-.116.555-.282.774-.482.21-.2.379-.441.496-.724.118-.283.177-.583.177-.915H178.4c-.059.865-.472 1.298-1.212 1.298zm-3.594 2.487v7.406h1.33l4.325-5.517v5.517h1.33v-7.406h-1.33l-4.325 5.517v-5.517h-1.33z"%0A    fill="%23000"%0A  />%0A</svg>%0A';var N="slideUpWidget.v1",x=class{constructor(t,i){this.localStorage=t}saveInLocalStorage(t){this.localStorage.setItem(N,JSON.stringify(t))}loadFromLocalStorage(){return this.localStorage.getItem(N)}loadBankDictionary(t){return b(this,null,function*(){try{return(yield fetch(t)).json()}catch(i){throw new Error("banksCacheIsEmpty")}})}getBankList(t){return b(this,null,function*(){try{let i=_(t),d=y(i);return(yield this.loadBankDictionary(d)).dictionary.map(a=>({bankName:a.bankName,logoURL:a.logoURL,dboLink:L(S(t),a)}))}catch(i){console.error(i)}})}showBankSelector(t){return b(this,null,function*(){this.closeWidget();let i=document.head,d=document.createElement("meta");d.setAttribute("id","widget-nspk"),d.setAttribute("name","viewport"),d.setAttribute("content","width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no"),i.appendChild(d);let r=yield this.getBankList(t),a=document.createElement("div");a.className="slide-up-widget";let u=document.createElement("div"),g=document.createElement("img"),c=document.createElement("div"),h=document.createElement("div");c.innerText=_(t)===w?m.SUBSCRIPTION_TITLE:m.PAYMENT_TITLE,h.innerText="\xD7",g.src=E,u.className="slide-up-widget__header",g.className="slide-up-widget__header-image",c.className="slide-up-widget__header-text",h.className="slide-up-widget__header-close-btn",h.addEventListener("click",()=>{this.closeWidget()}),u.appendChild(g),u.appendChild(h),u.appendChild(c),a.appendChild(u);let v=document.createElement("input");v.setAttribute("placeholder",m.ENTER_BANK_NAME),v.className="slide-up-widget__input",v.addEventListener("input",s=>{let o=s.target.value;if(o&&o.length>1){document.querySelectorAll(".slide-up-widget__bank-title").forEach(e=>{let p=e.closest(".slide-up-widget__bank"),f=p.className;e.innerText.toLowerCase().indexOf(o.toLowerCase())===-1||p.className.indexOf("used")!==-1?f.indexOf("hide")===-1&&(p.className=f+" slide-up-widget__bank--hide"):p.classList.remove("slide-up-widget__bank--hide")});let n=document.querySelector(".slide-up-widget__title--used");n&&n.className.indexOf("hide")===-1&&(n.className=n.className+" slide-up-widget__title--hide")}else{document.querySelectorAll(".slide-up-widget__bank--hide").forEach(e=>{e.classList.remove("slide-up-widget__bank--hide")});let n=document.querySelector(".slide-up-widget__title--used");n&&n.classList.remove("slide-up-widget__title--hide")}if(document.querySelectorAll(".slide-up-widget__bank--hide:not(.slide-up-widget__bank--used)").length>=r.length){if(!document.querySelector(".slide-up-widget__empty")){let n=document.createElement("div");n.innerText=m.NO_MATCHING_ITEMS,n.className="slide-up-widget__empty",a.appendChild(n)}}else document.querySelector(".slide-up-widget__empty")&&document.querySelector(".slide-up-widget__empty").remove()}),a.appendChild(v);let z=this.loadFromLocalStorage(),k=r;if(z){let s=JSON.parse(z),o=[];s.forEach(n=>{let e=k.find(p=>p.bankName===n);e&&o.push(e)}),k=[...o,...r.filter(n=>s.every(e=>n.bankName!==e))]}k.forEach(s=>{let o=document.createElement("a"),n=document.createElement("img"),e=document.createElement("div"),p=s.dboLink;o.className="slide-up-widget__bank",n.className="slide-up-widget__bank-logo",e.className="slide-up-widget__bank-title",o.setAttribute("href",p),n.src=s.logoURL,e.innerText=s.bankName,o.appendChild(n),o.appendChild(e),a.appendChild(o)}),a.addEventListener("click",s=>{console.log(s);let o=s.target.closest(".slide-up-widget__bank");if(o){let n=o.querySelector(".slide-up-widget__bank-title").innerText,e=JSON.parse(this.loadFromLocalStorage());if(!(e?e.some(f=>f===n):!0))(e==null?void 0:e.length)>2&&e.pop(),this.saveInLocalStorage([n,...e]);else if((e==null?void 0:e.length)>0){let f=e.splice(e.indexOf(n),1);this.saveInLocalStorage([...f,...e])}else this.saveInLocalStorage([n])}}),document.body.appendChild(a)})}closeWidget(){let t=document.head.querySelector("#widget-nspk");t&&t.remove();let i=document.querySelector(".slide-up-widget");i&&i.parentNode.removeChild(i)}};window.SlideUpWidget=x;})();
