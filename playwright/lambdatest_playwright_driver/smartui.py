from lambdatest_sdk_utils import is_smartui_enabled, fetch_dom_serializer, post_snapshot # type: ignore
from lambdatest_sdk_utils import setup_logger, get_logger # type: ignore
from playwright.async_api import Page # type: ignore

def smartui_snapshot(page: Page, name: str, options={}):
    # setting up logger
    setup_logger()
    logger = get_logger('lambdatest-playwright-driver')
    

    if not page:
        raise ValueError('A Playwright `page` object is required.')
    if not name:
        raise ValueError('The `snapshotName` argument is required.')
    if is_smartui_enabled() is False: 
        raise Exception("Cannot find SmartUI server.")
    
    try:
        resp = fetch_dom_serializer()
        page.evaluate(resp['data']['dom'])
                
        dom = dict()
        dom['name'] = name
        dom['url'] = page.url        
        dom['dom'] = page.evaluate("([options]) => SmartUIDOM.serialize(options)",[options])
        
        res = post_snapshot(dom, 'lambdatest-playwright-driver', options=options)

        if res and res.get('data') and res['data'].get('warnings') and len(res['data']['warnings']) != 0:
            for warning in res['data']['warnings']:
                logger.warning(warning)

        logger.info(f'Snapshot captured {name}')
    except Exception as e:
        logger.error(f"SmartUI snapshot failed '{name}'")
        logger.error(e)


async def smartui_snapshot_async(page: Page, name: str, options={}):
    # Async counterpart of smartui_snapshot for callers using playwright.async_api.
    # Same contract; awaits the two page.evaluate calls so the DOM serializer
    # is actually injected and the serialized DOM is captured (not a coroutine).
    setup_logger()
    logger = get_logger('lambdatest-playwright-driver')

    if not page:
        raise ValueError('A Playwright `page` object is required.')
    if not name:
        raise ValueError('The `snapshotName` argument is required.')
    if is_smartui_enabled() is False:
        raise Exception("Cannot find SmartUI server.")

    try:
        resp = fetch_dom_serializer()
        await page.evaluate(resp['data']['dom'])

        dom = dict()
        dom['name'] = name
        dom['url'] = page.url
        dom['dom'] = await page.evaluate("([options]) => SmartUIDOM.serialize(options)", [options])

        res = post_snapshot(dom, 'lambdatest-playwright-driver', options=options)

        if res and res.get('data') and res['data'].get('warnings') and len(res['data']['warnings']) != 0:
            for warning in res['data']['warnings']:
                logger.warning(warning)

        logger.info(f'Snapshot captured {name}')
    except Exception as e:
        logger.error(f"SmartUI snapshot failed '{name}'")
        logger.error(e)
