(window.webpackJsonp=window.webpackJsonp||[]).push([[46],{"4X/0":function(module,e,t){"use strict";t.d(e,"a",function(){return a});var n=function clearCacheWithTypename(e,t){var n=new RegExp("^".concat(t));Object.keys(e.data.data).forEach(function(t){return t.match(n)&&e.data.delete(t)})},a=function clearCacheWithTypenames(e,t){t.forEach(function(t){return n(e,t)})}},"8qrn":function(module,exports,e){},"951z":function(module,exports,e){},"9wTT":function(module,exports,e){var t=e("8qrn"),n;"string"==typeof t&&(t=[[module.i,t,""]]);var a={transform:void 0},r=e("aET+")(t,a);t.locals&&(module.exports=t.locals)},Bufl:function(module,e,t){"use strict";t.d(e,"a",function(){return r});var n=t("4X/0"),a=function clearQuizApolloCache(e){Object(n.a)(e.cache,["RestQuizSessionMetadataElement","RestQuizQuestionDataElement","LocalTimerState","LocalChangedResponse","LocalStepState"])},r=function clearPracticeQuizApolloCache(e){Object(n.a)(e.cache,["LocalChangedResponse","LocalStepState"])};e.b=a},FkXZ:function(module,exports,e){var t=e("951z"),n;"string"==typeof t&&(t=[[module.i,t,""]]);var a={transform:void 0},r=e("aET+")(t,a);t.locals&&(module.exports=t.locals)},QAEO:function(module,exports,e){},SpSO:function(module,e,t){"use strict";var n=t("sbe7"),a=t.n(n),r=t("qhBR"),i=t("w+/x"),o=t("USJv"),c=t("m10x"),l=t("kvW3"),s=t("d3Ej"),m=t.n(s),u=t("FkXZ"),p=t.n(u),d=Object(r.a)("CoverPageNudges"),f=function LikelihoodNudge(e){var t=e.value,n=Math.ceil(t/100);return a.a.createElement("div",{className:d()},a.a.createElement("div",{className:d("svg-icon")},a.a.createElement(o.a,{size:48})),a.a.createElement("div",{className:d("message")},a.a.createElement(c.i,null,m()("Get closer to your goal")),a.a.createElement(l.b,{message:m()("You are {value} more likely to complete the course if you finish the assignment"),value:a.a.createElement("strong",null,n>1?n+m()(" times"):t+"%"),tagName:"p",rootClassName:d("info")})))},v=function SocialNudge(e){var t=e.value;return a.a.createElement("div",{className:d()},a.a.createElement("div",{className:d("svg-icon")},a.a.createElement(i.a,{size:48}),","),a.a.createElement("div",{className:d("message")},a.a.createElement(c.i,null,m()("People are making progress")),a.a.createElement(l.b,{message:m()("{numOfLearners} learners have recently completed this assignment"),numOfLearners:a.a.createElement("strong",null,t),tagName:"p",rootClassName:d("info")})))},g=function CoverPageNudges(e){var t=e.nudge,n=t.nudgeType,r=t.nudgeNumber;switch(n){case"social":return a.a.createElement(v,{value:r});case"likelihood":return a.a.createElement(f,{value:r});default:return null}};e.a=g},USJv:function(module,e,t){"use strict";var n=t("sbe7"),a=t.n(n),r=t("MnCE"),i=t("oyNZ");function _extends(){return(_extends=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}function _objectWithoutProperties(e,t){if(null==e)return{};var n=_objectWithoutPropertiesLoose(e,t),a,r;if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++){if(a=i[r],t.indexOf(a)>=0)continue;if(!Object.prototype.propertyIsEnumerable.call(e,a))continue;n[a]=e[a]}}return n}function _objectWithoutPropertiesLoose(e,t){if(null==e)return{};var n={},a=Object.keys(e),r,i;for(i=0;i<a.length;i++){if(r=a[i],t.indexOf(r)>=0)continue;n[r]=e[r]}return n}var o=function SvgaChart(e){var t=e.title,a=void 0===t?"Chart":t,r=_objectWithoutProperties(e,["title"]);return n.createElement(i.a,_extends({title:a},r,{viewBox:"0 0 41 37"}),n.createElement("g",{fill:"none",fillRule:"evenodd"},n.createElement("path",{fill:"#F26C75",d:"M5 32h32V0H5z"}),n.createElement("path",{stroke:"#424242",strokeWidth:"2",d:"M8 28l9.263-12.572 10.105 8.98L40 6"}),n.createElement("path",{stroke:"#4D4D4D",strokeWidth:"2",d:"M1 0v36h40"})))};(o=Object(r.pure)(o)).displayName="SvgaChart",e.a=o},WrZC:function(module,e,t){"use strict";(function(n){var a=t("UB5X"),r=t.n(a),i=t("qhBR"),o=t("AWZ4"),c=t("m10x"),l=t("CsdX"),s=t("CfbJ"),m=t("d3Ej"),u=t.n(m),p=t("vRSd"),d=t("kvW3"),f=t("lEg3"),v=t("u/OM"),g=t("9wTT"),b=t.n(g),h=Object(i.a)("CoverPageRowRightSideActions"),E=function renderActionButton(e,t){return n.createElement(o.b,{size:"sm",type:"primary",label:e,onClick:t})},y=function CoverPageRowRightSideActions(e){var t=e.startAttempt,a=e.restartAttempt,i=e.resumeAttempt,m=e.retryAttempt,g=e.submissionTime,b=e.showTimer,y=e.timeLimit,L=e.timerId,S=e.attemptsLeft,C=e.secondsLeftInLatestAttempt,O=e.attemptLimitTimeLeft,P=null,j=r()(O)||"number"==typeof S&&0===S;return t?P=E(u()("Start"),t):a?P=E(u()("Restart"),a):i?P=E(u()("Resume"),i):m&&(P=n.createElement(o.b,{size:"sm",type:"link",label:u()("Try again"),onClick:m,disabled:j})),n.createElement("div",{className:h()},n.createElement("div",{className:h("action-button",{linkStyle:!!m})},P),j&&r()(O)&&n.createElement("div",{className:h("retry-info")},n.createElement(c.a,null,n.createElement(d.b,{message:u()("Retake the quiz in {attemptLimitTimeLeft}"),attemptLimitTimeLeft:n.createElement("strong",null,Object(f.c)(O))}))),g&&n.createElement("div",{className:h("submission-time")},n.createElement(c.a,null,n.createElement(c.g,{tag:"span"},u()("Submitted"))," ",n.createElement("span",{className:h("submission-time-detail")},p.a.getFormattedDeadline(g)))),r()(y)&&t&&n.createElement("div",{className:h("time-limit")},n.createElement(c.a,null,n.createElement(s.a,{size:20,color:l.b.primary}),n.createElement("span",{className:h("time-limit-text")},n.createElement(d.b,{message:u()("You will have {timeLimit} to finish"),timeLimit:Object(f.c)(y,!0)})))),b&&r()(C)&&n.createElement(v.b,{timerId:L,remainingTimeInMs:1e3*C,displayRemaining:!0}))};e.a=y}).call(this,t("sbe7"))},XSZB:function(module,exports,e){var t=e("QAEO"),n;"string"==typeof t&&(t=[[module.i,t,""]]);var a={transform:void 0},r=e("aET+")(t,a);t.locals&&(module.exports=t.locals)},pd9L:function(module,e,t){"use strict";t.r(e),t.d(e,"QuizCoverPage",function(){return I});var n=t("MVZn"),a=t.n(n),r=t("VbXa"),i=t.n(r),o=t("sbe7"),c=t.n(o),l=t("oJmH"),s=t.n(l),m=t("Bufl"),u=t("r4ax"),p=t("SpSO"),d=t("SNVJ"),f=t("scbn"),v=t("qJwm"),g=t("+LJP"),b=t("eV3f"),h=t("c5lh"),E=t("WrZC"),y=t("E8ls"),L=t("CtKc"),S=t("uZxl"),C=t("UCqf"),O=t("VtNW"),P=t.n(O),j=t("JkvR"),k=t("iFRF"),A=t("h0Uq"),w=t("pjUu"),N=t("TOZ3"),R=t("qhBR"),T=t("XSZB"),x=t.n(T),z=Object(R.a)("QuizCoverPage"),I=function(e){function QuizCoverPage(){for(var t,n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(t=e.call.apply(e,[this].concat(r))||this).getRestartAttemptFunction=function(e,n,r){return function(){if(n&&r){if(r.isLastAttemptBeforeLock||1===r.attemptsLeft)return void n({type:w.a.lastAttemptModal,props:a()({},r,{onPrimaryButtonClick:t.getRestartAttemptFunction(e)})});if("number"==typeof r.timeLimit)return void n({type:w.a.timedAttemptStart,props:a()({},r,{onPrimaryButtonClick:t.getRestartAttemptFunction(e)})})}var i=t.props.openAttemptPage;Object(m.b)(e),i()}},t}var t;return i()(QuizCoverPage,e),QuizCoverPage.prototype.render=function render(){var e=this,t=this.props,n=t.children,a=t.openSubmittedAttemptPage;return c.a.createElement(L.a,null,function(t){var r=t.item;if(!r||!r.contentSummary)return c.a.createElement(j.a,null);return c.a.createElement(S.a,{courseId:r.courseId,itemId:r.id},function(t){var i=t.loading,o=t.lastSessionId,s=t.lockingConfigurationSummary,g=t.unsubmittedSessionId,L=t.bestEvaluation,S=t.nudge,O=t.refetch;if(!r||!r.contentSummary||i)return c.a.createElement(j.a,null);if("exam"===r.contentSummary.typeName){var R,T=r.contentSummary.definition,x=r.isCumulativeGraded;return c.a.createElement(d.a,null,c.a.createElement(N.b,{justifyContent:"between",rootClassName:z("header-container")},c.a.createElement(u.a,{assignmentTypeName:P()("Quiz"),item:r}),S&&c.a.createElement(p.a,{nudge:S})),c.a.createElement(C.a,{standardProctorConfigurationId:T.standardProctorConfigurationId},function(t){var n=t.loading,a=t.timeLimit,i=t.secondsLeftInLatestAttempt,l=t.remainingAttempts,m=t.completedAttempts,u=t.client;return c.a.createElement(b.b,{stepTitle:P()("Submit your assignment"),stepDetails:c.a.createElement(h.a,{deadline:r.deadline,attemptsRateCount:null==s?void 0:s.allowedSubmissionsPerInterval,attemptsRateInterval:null==s?void 0:s.allowedSubmissionsInterval,attemptsLeft:l,attemptsCompleted:m}),rightSideView:c.a.createElement(w.b,null,function(t){var n=t.showModal,m={timeLimit:a,attemptsLeft:l,lockedTimeLeft:Object(A.b)(s),isLastAttemptBeforeLock:Object(A.c)(s),hasAttemptLimit:!!s&&s.allowedSubmissionsPerInterval>0};return c.a.createElement(E.a,{startAttempt:o||g?void 0:e.getRestartAttemptFunction(u,n,m),resumeAttempt:g?e.getRestartAttemptFunction(u):void 0,timeLimit:a,showTimer:!!g,timerId:Object(k.a)(r.id),secondsLeftInLatestAttempt:i,retryAttempt:e.getRestartAttemptFunction(u,n,m),attemptLimitTimeLeft:Object(A.a)(s),attemptsLeft:l})}),statusIconType:o?b.a.check:void 0})}),c.a.createElement(b.b,{stepTitle:P()("Receive grade"),stepDetails:c.a.createElement(h.a,{passingFraction:T.passingFraction,isCumulativeGraded:x}),rightSideView:c.a.createElement(l.ApolloConsumer,null,function(e){return c.a.createElement(y.a,{itemGrade:r.itemGrade,computedScore:null==L?void 0:L.score,maxScore:null==L?void 0:L.maxScore,isCumulativeGraded:x,viewFeedback:o?function(){Object(m.b)(e),a()}:void 0,isViewFeedbackButtonLinkStyle:!!g})}),statusIconType:Object(b.c)(null===(R=r.itemGrade)||void 0===R?void 0:R.isPassed,x)}),c.a.createElement(b.b,{rightSideView:c.a.createElement(f.a,{computedItem:r,itemFeedbackType:v.m.Quiz})}),n&&c.a.cloneElement(n,{refetchCoverPageData:function refetchCoverPageData(){return O().then(function(){return r.refetch()})}}))}return null})})},QuizCoverPage}(c.a.Component);e.default=Object(g.a)(function(e){return{openAttemptPage:function openAttemptPage(){e.push({name:"quiz-attempt",params:e.params})},openSubmittedAttemptPage:function openSubmittedAttemptPage(){e.push({name:"quiz-view-attempt",params:e.params})}}})(I)},"w+/x":function(module,e,t){"use strict";var n=t("sbe7"),a=t.n(n),r=t("MnCE"),i=t("oyNZ");function _extends(){return(_extends=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}function _objectWithoutProperties(e,t){if(null==e)return{};var n=_objectWithoutPropertiesLoose(e,t),a,r;if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++){if(a=i[r],t.indexOf(a)>=0)continue;if(!Object.prototype.propertyIsEnumerable.call(e,a))continue;n[a]=e[a]}}return n}function _objectWithoutPropertiesLoose(e,t){if(null==e)return{};var n={},a=Object.keys(e),r,i;for(i=0;i<a.length;i++){if(r=a[i],t.indexOf(r)>=0)continue;n[r]=e[r]}return n}var o=function SvgaPen(e){var t=e.title,a=void 0===t?"Pen":t,r=_objectWithoutProperties(e,["title"]);return n.createElement(i.a,_extends({title:a},r,{viewBox:"0 0 36 44"}),n.createElement("g",{fill:"none",fillRule:"evenodd"},n.createElement("path",{d:"M36 25.855C36 35.845 20.836 44 10.895 44S0 35.846 0 25.855C0 15.865 13.185 8 23.127 8 33.067 8 36 15.864 36 25.855",fill:"#F3C800"}),n.createElement("path",{stroke:"#4D4D4D",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",d:"M21.907 4.781l6.751 12.248-10.823 17.146L7.253 17.181l6.999-12.452M8.428 4.081h19.359V1H8.427zM17.954 33.074V21.186"}),n.createElement("path",{d:"M15.23 18.272a2.723 2.723 0 1 1 5.447 0 2.723 2.723 0 0 1-5.446 0z",stroke:"#4D4D4D",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"})))};(o=Object(r.pure)(o)).displayName="SvgaPen",e.a=o}}]);
//# sourceMappingURL=46.2807f415fb5c003c50d5.js.map