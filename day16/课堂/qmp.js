function Va(e, t=null, n=null, r=0, s=null, o=e === Fe ? 0 : 1, i=!1, a=!1) {
    const l = {
        __v_isVNode: !0,
        __v_skip: !0,
        type: e,
        props: t,
        key: t && Ba(t),
        ref: t && kn(t),
        scopeId: ar,
        slotScopeIds: null,
        children: n,
        component: null,
        suspense: null,
        ssContent: null,
        ssFallback: null,
        dirs: null,
        transition: null,
        el: null,
        anchor: null,
        target: null,
        targetAnchor: null,
        staticCount: 0,
        shapeFlag: o,
        patchFlag: r,
        dynamicProps: s,
        dynamicChildren: null,
        appContext: null,
        ctx: be
    };
    return a ? (Ns(l, n),
    o & 128 && e.normalize(l)) : n && (l.shapeFlag |= ye(n) ? 8 : 16),
    bn > 0 && !i && qe && (l.patchFlag > 0 || o & 6) && l.patchFlag !== 32 && qe.push(l),
    l
}