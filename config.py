

# 参考代码：https://www.cnblogs.com/pythonfm/p/9056461.html
ALF = 1583630252
MLOGIN = 1
M_WEIBOCN_PARAMS = 'oid%3D4469046194244186%26luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803'
SCF = 'AjheAPuZRqxmyLT-kTVnBXGduebXE6nZGT5fS8_VPbfADyWHQ_WyoRzZqAJNujugOFYP1tUivrlzK2TGTx83_Qo.'
SSOLoginState = 1581038313
SUB = '_2A25zOMq5DeRhGeNM6FUX8S_EzDqIHXVQwtbxrDV6PUJbktAKLVPhkW1NTjKs6wgXZoFv2vqllQWpcwE-e9-8LlMs'
SUBP = '0033WrSXqPxfM725Ws9jqgMF55529P9D9W58TWlXMj17lMMvjhSsjQ1p5JpX5K-hUgL.Fo-Ee0MceK2RS0q2dJLoIEXLxKqLBozL1h.LxKML1-BLBK2LxKML1-2L1hBLxK-LBKqL12BLxK-LBKqL12Bt'
SUHB = '0BLYTPzIKSGsDo'
WEIBOCN_FROM = 1110006030
XSRF_TOKEN = '5dcf70'
_T_WM = 64204543757
Cookie = {
    'Cookie': 'ALF={:d};MLOGIN={:d};M_WEIBOCN_PARAMS={};SCF={};SSOLoginState={:d};SUB={};SUBP={};SUHB={};WEIBOCN_FROM={:d};XSRF-TOKEN={};_T_WM={:d};'.format(
        ALF,
        MLOGIN,
        M_WEIBOCN_PARAMS,
        SCF,
        SSOLoginState,
        SUB,
        SUBP,
        SUHB,
        WEIBOCN_FROM,
        XSRF_TOKEN,
        _T_WM
    )
}

headers = {
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 通过ajax请求形式获取数据
    'X-XSRF-TOKEN': 'aa8bed',
    'Accept': 'application/json, text/plain, */*',
    'Connection': 'close'
}
