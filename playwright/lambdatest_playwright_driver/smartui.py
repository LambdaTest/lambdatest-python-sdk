from lambdatest_sdk_utils import is_smartui_enabled, fetch_dom_serializer, post_snapshot
from lambdatest_sdk_utils import get_pkg_name, setup_logger, get_logger
from playwright.async_api import Page, Error

async def smartui_snapshot(page: Page, name: str, options={}):
    # setting up logger
    setup_logger()
    logger = get_logger()

    if not page:
        raise ValueError('A Playwright `page` object is required.')
    if not name:
        raise ValueError('The `snapshotName` argument is required.')
    if not await is_smartui_enabled():
        raise Exception("Cannot find SmartUI server.")
    
    try:
        resp = fetch_dom_serializer()
        await page.evaluate(resp['data']['dom'])

        # Serialize and capture the DOM
        dom = await page.evaluate(f"""
        return {{
            dom: SmartUIDOM.serialize({options}),
            url: page.url()
        }}
        """)

        # Post the dom to smartui endpoint
        dom['name'] = name
        res = await post_snapshot(dom, get_pkg_name(), options=options)

        if res and res.get('data') and res['data'].get('warnings') and len(res['data']['warnings']) != 0:
            for warning in res['data']['warnings']:
                logger.warning(warning)

        logger.info(f'Snapshot captured {name}')
    except Exception as e:
        logger.error(f"SmartUI snapshot failed '{name}'")
        logger.error(str(e))

