(window.webpackJsonp=window.webpackJsonp||[]).push([[50,48],{"9u2/":function(module,e,t){"use strict";t.r(e),t.d(e,"AttemptPage",function(){return z}),t.d(e,"withRedirectToCover",function(){return T});var n=t("VbXa"),a=t.n(n),i=t("sbe7"),r=t.n(i),s=t("qhBR"),o=t("m10x"),u=t("+LJP"),m=t("uZxl"),c=t("DA/5"),d=t("hJJs"),l=t("8PFk"),f=t("1p0w"),p=t("awXj"),v=t("mtFd"),b=t("Z1YL"),S=t("pGb1"),g=t("CtKc"),D=t("wuov"),I=t("UCqf"),y=t("xe4q"),h=t("iFRF"),E=t("ZoCu"),Q=t("VtNW"),C=t.n(Q),x=t("3AUy"),A=t.n(x),R=Object(s.a)("AttemptPage"),z=function(e){function AttemptPage(){return e.apply(this,arguments)||this}a()(AttemptPage,e);var t=AttemptPage.prototype;return t.componentDidMount=function componentDidMount(){var e=this.props,t=e.shouldRedirectToCover,n=e.redirectToCover;t&&n()},t.render=function render(){var e=this.props,t=e.redirectToCover,n=e.addRedirectToCoverToRouteParams,a=e.examSessionId;return r.a.createElement(g.a,null,function(e){var i=e.item;if(!i)return null;return r.a.createElement(I.a,{standardProctorConfigurationId:i.contentSummary&&"exam"===i.contentSummary.typeName&&i.contentSummary.definition.standardProctorConfigurationId||null},function(e){var s=e.shouldShowTimer,u=e.timeLimit,g=e.secondsLeftInLatestAttempt,I=e.refetch,Q=e.remainingAttempts;return r.a.createElement(f.a,{onClose:t,headerLeft:r.a.createElement(c.a,{headerText:i.name,itemTypeText:C()("Graded Quiz"),timeCommitment:i.timeCommitment}),headerRight:r.a.createElement(v.a,{courseId:i.courseId,itemId:i.id,examSessionId:a},function(e){var t=e.isSubmitted;return r.a.createElement(d.a,{deadline:i.deadline,remainingTimeInMs:"number"==typeof g?1e3*g:null,showTimer:s&&!t,timerId:Object(h.a)(i.id),examSessionId:a})}),topBanner:r.a.createElement(v.a,{courseId:i.courseId,itemId:i.id,examSessionId:a},function(e){var n=e.isSubmitted,a=e.client,s,o=(i.contentSummary&&"exam"===i.contentSummary.typeName&&i.contentSummary.definition||{}).passingFraction;if(n&&i.itemGrade)return r.a.createElement(m.a,{courseId:i.courseId,itemId:i.id},function(e){var n=e.lockingConfigurationSummary,a=e.bestEvaluation;return r.a.createElement(y.a,{itemGrade:i.itemGrade,computedScore:null==a?void 0:a.score,maxScore:null==a?void 0:a.maxScore,passingFraction:o,isCumulativeGraded:i.isCumulativeGraded,onKeepLearningClick:t,remainingAttempts:Q,lockingConfigurationSummary:n,onTryAgainClick:t})});return null})},r.a.createElement(v.a,{courseId:i.courseId,itemId:i.id,onQuizSessionQueryCompleted:function onQuizSessionQueryCompleted(){return I()},examSessionId:a},function(e){var t=e.quizFormData,a=e.sessionId,u=e.nextSubmissionDraftId,m=e.attemptScore,c=e.totalPoints,d=e.isSubmitted,f=e.hasDraft,v=e.isLimitedFeedback;if(!t||!a)return r.a.createElement(D.a,null);if(v)return null;var g=t.map(function(e){return e.prompt.id});return r.a.createElement(S.a,{itemId:i.id,courseId:i.courseId},function(e){var v=e.stepState;return r.a.createElement("div",{className:R()},r.a.createElement("div",{className:R("header")},r.a.createElement(o.c,null,i.name),d&&"number"==typeof m?r.a.createElement("div",{className:R("submission-grade")},r.a.createElement(o.g,{tag:"span"},C()("Latest Submission Grade")),r.a.createElement("div",{className:R("grade-percent")},"".concat(Object(E.a)(m),"%"))):r.a.createElement(o.a,{rootClassName:R("points")},r.a.createElement(o.g,{tag:"span"},C()("Total points #{totalPoints}",{totalPoints:c})))),r.a.createElement("div",{className:R("prompts")},t.map(function(e,t){return r.a.createElement(p.a,{key:e.prompt.id,quizQuestion:e,index:t,isReadOnly:!!d,isDisabled:!!(null==v?void 0:v.isSaving)||!!(null==v?void 0:v.isSubmitting)})})),r.a.createElement(b.a,{ids:g,sessionId:a,nextSubmissionDraftId:u},function(e){var t=e.hasUnfilledResponses,a=e.saveDraft,o=e.autoSaveDraft,u=e.submitDraft,m=e.submitLatestSubmissionDraft;return r.a.createElement(l.a,{hasUnfilledResponses:t,itemId:i.id,courseId:i.courseId,saveDraft:a,autoSaveDraft:o,isSubmitted:d,submitDraft:function submitDraft(){return u?u().then(function(){n()}):Promise.reject()},submitLatestSubmissionDraft:function submitLatestSubmissionDraft(){return m?m().then(function(){n()}):Promise.reject()},hasTimer:s,hasDraft:f,stepState:v})}))})}))})})},AttemptPage}(r.a.Component),T=Object(u.a)(function(e,t){var n=t.refetchCoverPageData;return{redirectToCover:function redirectToCover(){n&&n(),e.push({name:"quiz-cover",params:e.params,query:e.location.query}),window.location.reload()},addRedirectToCoverToRouteParams:function addRedirectToCoverToRouteParams(){e.push({name:"quiz-attempt",params:e.params,query:{redirectToCover:!0}})},shouldRedirectToCover:e.location.query.redirectToCover}});e.default=T(z)},Qr3p:function(module,e,t){"use strict";var n=t("VkAN"),a=t.n(n),i=t("sbe7"),r=t.n(i),s=t("lTCR"),o=t.n(s),u=t("oJmH"),m=t.n(u);function _templateObject(){var e=a()(['\n  mutation QuizActions($sessionId: String!, $body: String!, $skipQuestionsField: Boolean!) {\n    action(sessionId: $sessionId, body: $body)\n      @rest(\n        type: "QuizActionData"\n        path: "onDemandExamSessions.v1/{args.sessionId}/actions"\n        method: "POST"\n        bodyKey: "body"\n      ) {\n      elements @type(name: "RestQuizQuestionDataElement") {\n        id\n        result @type(name: "RestQuizQuestionDataElementResult") {\n          nextSubmissionDraftId\n          evaluation\n          questions @skip(if: $skipQuestionsField)\n        }\n      }\n    }\n  }\n']);return _templateObject=function _templateObject(){return e},e}var c=o()(_templateObject()),d=function getSaveDraftMutation(e){return function(t,n,a){return e({variables:{body:{argument:{id:t,input:{responses:a}},name:"saveSubmissionDraft"},sessionId:n,skipQuestionsField:!0}})}},l=function getSubmitDraftMutation(e){return function(t,n){return e({variables:{body:{argument:{responses:n},name:"submitResponses"},sessionId:t,skipQuestionsField:!1}})}},f=function getAutoSubmitDraftMutation(e){return function(t){return e({variables:{body:{argument:{},name:"submitLatestSubmissionDraft"},sessionId:t,skipQuestionsField:!1}})}},p=function QuizMutations(e){var t=e.children;return r.a.createElement(u.Mutation,{mutation:c},function(e){var n=d(e),a=l(e),i=f(e);return t({saveDraftMutation:n,submitDraftMutation:a,autoSubmitDraftMutation:i})})};e.a=p},Z1YL:function(module,e,t){"use strict";var n=t("sbe7"),a=t.n(n),i=t("cXyc"),r=t("pGb1"),s=t("r1db"),o=t("CtKc"),u=t("uZxl"),m=t("Qr3p"),c=function QuizActions(e){var t=e.ids,n=e.sessionId,c=e.children,d=e.nextSubmissionDraftId;return a.a.createElement(o.a,null,function(e){var o=e.item;if(!o)return null;var l=o.courseId,f=o.id;return a.a.createElement(u.a,{courseId:l,itemId:f},function(e){var u=e.refetch;return a.a.createElement(i.a,{ids:t},function(e){if(!e||!u)return c({});var t=e.some(function(e){var t,n;return!(null==e?void 0:null===(t=e.response)||void 0===t?void 0:null===(n=t.definition)||void 0===n?void 0:n.value)});return a.a.createElement(r.a,{itemId:f,courseId:l},function(i){var r=i.stepState,l=i.setStepState;return a.a.createElement(m.a,null,function(i){var m=i.saveDraftMutation,f=i.submitDraftMutation,p=i.autoSubmitDraftMutation,v=e.map(function(e){var t,n;return{questionInstance:e.id,response:null===(t=e.response)||void 0===t?void 0:null===(n=t.definition)||void 0===n?void 0:n.value}}),b=function saveDraft(){if(!r.isSaving&&!r.isSubmitting&&d)return l({isSaving:!0}),m(d,n,v).then(function(){return l({isSaving:!1})});return Promise.reject()},S=function autoSaveDraft(){if(!r.isAutoSaving&&!r.isSubmitting&&d)return l({isAutoSaving:!0}),m(d,n,v).then(function(){return l({isAutoSaving:!1})});return Promise.reject()},g=function refetchItemAndExamSummary(){return u().then(function(){return o.refetch()})},D=function submitDraft(){if(!r.isSubmitting)return l({isSubmitting:!0}),f(n,v).then(function(){return l({isSubmitting:!1})}).then(g);return Promise.reject()},I=function submitLatestSubmissionDraft(){if(!r.isSubmitting)return l({isSubmitting:!0}),p(n).then(function(){return l({isSubmitting:!1})}).then(g);return Promise.reject()};return a.a.createElement(s.a,{stepState:r,saveDraft:S,changedResponses:e},function(){return c({hasUnfilledResponses:t,saveDraft:b,autoSaveDraft:S,submitDraft:D,submitLatestSubmissionDraft:I})})})})})})})};e.a=c},c01e:function(module,e,t){"use strict";t.r(e);var n=t("sbe7"),a=t.n(n),i=t("PDuk"),r=t.n(i),s=t("CtKc"),o=t("uZxl"),u=t("9u2/"),m=function SubmittedAttemptPage(){return a.a.createElement(s.a,null,function(e){var t=e.item;if(!t||!t.contentSummary)return null;return a.a.createElement(o.a,{courseId:t.courseId,itemId:t.id},function(e){var n=e.loading,r=e.lastSessionId;if(n)return null;var s=Object(i.tupleToStringKey)([t.courseId,t.id,r]);return a.a.createElement(u.default,{examSessionId:s})})})};e.default=m},mtFd:function(module,e,t){"use strict";(function(n){t.d(e,"a",function(){return l});var a=t("VkAN"),i=t.n(a),r=t("lTCR"),s=t.n(r),o=t("oJmH"),u=t.n(o),m=t("McCs");function _templateObject2(){var e=i()(['\n  query QuizDataQuery(\n    $sessionId: String!\n    $questionDataArgs: String!\n    $responseDataArgs: String!\n    $skipFetchingResponses: Boolean!\n  ) {\n    quizQuestionData(sessionId: $sessionId, questionDataArgs: $questionDataArgs)\n      @rest(\n        type: "QuizQuestionData"\n        path: "onDemandExamSessions.v1/{args.sessionId}/actions"\n        method: "POST"\n        bodyKey: "questionDataArgs"\n      ) {\n      elements @type(name: "RestQuizQuestionDataElement") {\n        id\n        result @type(name: "RestQuizQuestionDataElementResult") {\n          questions\n          nextSubmissionDraftId\n          evaluation\n          responses(sessionId: $sessionId, responseDataArgs: $responseDataArgs)\n            @skip(if: $skipFetchingResponses)\n            @rest(\n              type: "QuizResponseData"\n              path: "onDemandExamSessions.v1/{args.sessionId}/actions"\n              method: "POST"\n              bodyKey: "responseDataArgs"\n            ) {\n            elements @type(name: "RestQuizResponseDataElement") {\n              id\n              result\n            }\n          }\n        }\n      }\n    }\n  }\n']);return _templateObject2=function _templateObject2(){return e},e}function _templateObject(){var e=i()(['\n  query QuizSessionMetaDataQuery($body: String!) {\n    quizSessionMetaData(body: $body)\n      @rest(type: "RestQuizSessionMetadata", path: "onDemandExamSessions.v1", method: "POST", bodyKey: "body") {\n      elements @type(name: "RestQuizSessionMetadataElement") {\n        id\n      }\n    }\n  }\n']);return _templateObject=function _templateObject(){return e},e}var c=s()(_templateObject()),d=s()(_templateObject2()),l=function QuizData(e){var t=e.courseId,a=e.itemId,i=e.examSessionId,r=e.children,s=e.onQuizSessionQueryCompleted,u={courseId:t,itemId:a},l={argument:[],name:"getState"},f={argument:[],name:"getLatestSubmissionDraft"};return n.createElement(o.Query,{query:c,variables:{body:u},onCompleted:s,skip:!!i},function(e){var t=e.loading,a=e.data,s=e.refetch;if(t&&!i)return r({loading:t});var u=i||a.quizSessionMetaData.elements[0].id;return n.createElement(o.Query,{query:d,variables:{sessionId:u,questionDataArgs:l,responseDataArgs:f,skipFetchingResponses:!!i}},function(e){var t=e.loading,n=e.data,a=e.refetch,o=e.client;if(t)return r({loading:t});var c=n.quizQuestionData.elements[0].result,d=c.questions,l=c.responses,f=c.nextSubmissionDraftId,p=c.evaluation,v=null==l?void 0:l.elements[0].result.draft.input.responses,b=Object(m.a)(d,v,!!i),S=p&&p.score/p.maxScore,g=(null==p?void 0:p.maxScore)||b.reduce(function(e,t){return e+t.prompt.weightedScoring.maxScore},0),D=!d[0].isSubmitAllowed,I="NoDetails"===d[0].variant.detailLevel,y,h;return r({loading:t,quizFormData:b,sessionId:u,nextSubmissionDraftId:f,isSubmitted:D,isLimitedFeedback:I,attemptScore:S,totalPoints:g,hasDraft:!!v,refetchQuizData:function refetchQuizData(){return s().then(function(){return a()})},client:o})})})},f=l}).call(this,t("sbe7"))}}]);
//# sourceMappingURL=50.89f1fc864f26d8c69d19.js.map