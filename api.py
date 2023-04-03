
import requests



class ApiPro5:
    def __init__(self, cookies) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            self.jazoet = profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            self.user_id = profile.split('","viewer_actor":{"__typename":"User","id":"')[1].split('"},"')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
            self.jazoet = profile.split('&jazoest=')[1].split('","e":"')[0]
            self.user_id = profile.split('{"u":"\/ajax\/qm\/?__a=1&__user=')[1].split('&__comet_req=')[0]
    def reaction(self, id_post, type):
        if type == 'LIKE':
            reac = '1635855486666999'
        elif type ==  'LOVE':
            reac  =  '1678524932434102'
        elif type ==  'CARE':
            reac = '613557422527858'
        elif type ==  'HAHA':
            reac = '115940658764963'
        elif type ==  'WOW':
            reac = '478547315650144'
        elif type ==  'SAD':
            reac = '908563459236466'
        elif type ==  'ANGRY':
            reac = '444813342392137'
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reac+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'type': type, 'url': url}
        except:
            return {'status': False, 'type': type, 'url': url}
            
            
            
            

cookies='sb=yC69Y0rf5sABJNh0EqDcyK1Q; datr=yC69Y1SWztuy8pGCP01mAfJQ; vpd=v1;724x384x1.875; c_user=100089801793694; xs=26:JGFGBkSVX542cA:2:1680175532:-1:6338; fr=02BImBWjyCSgQ8l67.AWWicnwVDnrGM4GxIhW8MNCzGlU.Bj92jR.HU.AAA.0.0.BkJXGs.AWXQysowcWQ; m_page_voice=100089801793694;i_user=100091261340369&mibextid=ZbWKwL
'
api = ApiPro5(cookies)
ai=api.reaction(id, type)