from playwright.sync_api._generated import Browser
import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()
    
@pytest.fixture
def context(browser: Browser, request):
    # Buat folder hasil
    video_dir = Path("test-results/videos")
    trace_dir = Path("test-results/traces")

    video_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    # Buat browser context dengan video recording
    context = browser.new_context(
        record_video_dir=str(video_dir)
    )

    # Mulai tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    # Stop tracing
    context.tracing.stop(
        path=str(trace_dir / f"{request.node.name}.zip")
    )

    # Close context agar video tersimpan
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()

    yield page

    page.close()