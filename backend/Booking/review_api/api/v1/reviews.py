from fastapi import APIRouter, Depends, status

from models.reviews import Review
from utils import auth


router = APIRouter()
auth_handler = auth.AuthHandler()


@router.post(
    '/reviews/{event_id}',
    summary='Создание отзыва на событие',
    description='Создание отзыва',
    response_model=Review,
    response_description='Полное ревью события',
)
async def create_review(
    event_id: str,
    _user: dict = Depends(auth_handler.auth_wrapper),
) -> Review:
    return status.HTTP_201_CREATED


@router.put(
    '/reviews/{event_id}/{review_id}',
    summary='Изменение отзыва на событие',
    description='Изменение отзыва',
    response_model=Review,
    response_description='Обновлённое ревью события',
)
async def update_review(
    event_id: str,
    review_id: str,
    _user: dict = Depends(auth_handler.auth_wrapper),
) -> Review:
    return status.HTTP_200_OK


@router.get(
    '/reviews/{event_id}/{review_id}',
    summary='Получение отзыва на событие',
    description='Получение отзыва',
    response_model=Review,
    response_description='Ревью события',
)
async def get_review(
    event_id: str,
    review_id: str,
    _user: dict = Depends(auth_handler.auth_wrapper),
) -> Review:
    return status.HTTP_200_OK


@router.get(
    '/reviews/{event_id}',
    summary='Получение всех отзывов на событие',
    description='Получение всех отзывов',
    response_model=Review,
    response_description='Список ревью события',
)
async def get_reviews(
    event_id: str,
    _user: dict = Depends(auth_handler.auth_wrapper),
) -> Review:
    return status.HTTP_200_OK
